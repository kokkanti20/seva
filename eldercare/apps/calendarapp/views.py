from django.shortcuts import render
from datetime import date, datetime
import calendar
from .models import Event

def calendar_view(request):
    today = date.today()

    # Get year and month from query params, default is current year/month
    year = int(request.GET.get("year", today.year))
    month = int(request.GET.get("month", today.month))

    # Calendar matrix for given month
    cal = calendar.Calendar()
    month_days = cal.itermonthdates(year, month)

    # Fetch events for this month
    events = Event.objects.filter(date__year=year, date__month=month)

    context = {
        "year": year,
        "month": month,
        "month_name": calendar.month_name[month],
        "month_days": month_days,
        "events": events,
    }
    return render(request, "calendarapp/calendar_month.html", context)
