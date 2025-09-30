from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import EmergencyContact, SOSAlert

def phone_to_sms_email(phone: str, carrier: str) -> str | None:
    """
    Map phone + carrier -> email gateway address. Returns None if unknown carrier.
    """
    gateways = getattr(settings, "SMS_GATEWAYS", {})
    gateway = gateways.get(carrier)
    if gateway and phone:
        digits = "".join([c for c in phone if c.isdigit()])
        return f"{digits}@{gateway}"
    return None


@login_required
def sos_home(request):
    return render(request, "sos/home.html")


@login_required
@require_POST
def sos_send(request):
    user = request.user
    lat = request.POST.get("lat")
    lng = request.POST.get("lng")
    note = request.POST.get("note", "").strip()

    # Build message
    loc_line = f"Location: https://maps.google.com/?q={lat},{lng}" if lat and lng else ""
    msg = f"🚨 SOS Alert from {user.username}\n{loc_line}\n"
    if note:
        msg += f"Note: {note}\n"

    # Get contacts
    contacts = EmergencyContact.objects.filter(user=user)
    if not contacts.exists():
        return HttpResponseBadRequest("No emergency contacts set for this user.")

    to_emails = []
    for c in contacts:
        if c.phone and c.carrier:
            sms_email = phone_to_sms_email(c.phone, c.carrier)
            if sms_email:
                to_emails.append(sms_email)
        if c.email:
            to_emails.append(c.email)

    if not to_emails:
        return HttpResponseBadRequest("Contacts exist but have no deliverable SMS/email addresses.")

    # Send email(s)
    send_mail(
        subject="🚨 SOS ALERT",
        message=msg,
        from_email=getattr(settings, "DEFAULT_FROM_EMAIL", "sos@eldercare.ai"),
        recipient_list=to_emails,
        fail_silently=False,
    )

    # Save log
    alert = SOSAlert.objects.create(
        user=user,
        message=msg,
        latitude=float(lat) if lat else None,
        longitude=float(lng) if lng else None,
        delivered_to=",".join(to_emails),
    )

    return JsonResponse({"ok": True, "alert_id": alert.id, "delivered_to": to_emails})
