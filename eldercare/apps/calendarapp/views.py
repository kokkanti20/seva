from datetime import date
import calendar
from django.shortcuts import render
from .models import Event   # ✅ add this line

def calendar_view(request):
    today = date.today()
    year = int(request.GET.get("year", today.year))
    month = int(request.GET.get("month", today.month))

    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1

    cal = calendar.Calendar()
    month_days = cal.itermonthdates(year, month)

    events = Event.objects.filter(date__year=year, date__month=month)

    context = {
        "year": year,
        "month": month,
        "month_name": calendar.month_name[month],
        "month_days": month_days,
        "events": events,
    }
    return render(request, "calendarapp/calendar_month.html", context)
