from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest

@csrf_exempt
def trigger_sos(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST only")
    to = request.POST.get("to","you@example.com")
    msg = request.POST.get("message","SOS: Please check on me.")
    send_mail("ELDERCARE SOS", msg, "noreply@eldercare.local", [to])
    return JsonResponse({"ok": True, "sent_to": to})
