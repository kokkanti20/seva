import re
from datetime import datetime, timedelta
from dateutil import parser as dtparser
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import make_aware, get_current_timezone
from apps.meds.models import Medication, MedSchedule, MedEvent

@csrf_exempt
def parse_med(request):
    """Very simple demo parser for text like:
    'Metformin 500mg 1 pill after food at 8am and 8pm'
    Returns JSON that can be used to prefill a MedSchedule form.
    Replace with your local LLM/NLU when ready.
    """
    if request.method != "POST":
        return HttpResponseBadRequest("POST only")
    body = request.body.decode("utf-8")
    name_match = re.search(r'([A-Za-z][A-Za-z0-9\- ]+)', body)
    dose_match = re.search(r'(\b\d+\s*(?:pill|pills|tablet|ml|mg)\b)', body, flags=re.I)
    food = "after" if "after" in body.lower() else ("before" if "before" in body.lower() else "")
    times = re.findall(r'(\b\d{1,2}\s*(?:am|pm)\b)', body, flags=re.I)
    return JsonResponse({
        "name": name_match.group(1).strip() if name_match else "Unknown",
        "dose": dose_match.group(1) if dose_match else "1 pill",
        "instructions": f"{food} food" if food else "",
        "times": [t.lower().replace(" ", "") for t in times] or ["8am"],
    })

def weekly_summary(request, user_id:int):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponseBadRequest("User not found")
    tz = get_current_timezone()
    now = datetime.now(tz)
    week_start = (now - timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
    events = MedEvent.objects.filter(schedule__user=user, due_at__gte=week_start, due_at__lte=now)
    total = events.count()
    taken = events.filter(status='taken').count()
    pct = (taken/total*100) if total else 0
    return JsonResponse({
        "user": user.username,
        "week_start": week_start.isoformat(),
        "total_events": total,
        "taken_events": taken,
        "adherence_pct": round(pct,1),
        "summary_text": f"This week, you took {round(pct,1)}% of your medicines."
    })
