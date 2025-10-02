from django.shortcuts import render
from django.utils.timezone import now
from datetime import date, timedelta
from .models import Event

def calendar_view(request):
    today = date.today()
    current_year = today.year

    # Filter events by past, current, and next year
    past_year_events = Event.objects.filter(date__year=current_year - 1)
    current_year_events = Event.objects.filter(date__year=current_year)
    next_year_events = Event.objects.filter(date__year=current_year + 1)

    context = {
        "past_year": current_year - 1,
        "current_year": current_year,
        "next_year": current_year + 1,
        "past_year_events": past_year_events,
        "current_year_events": current_year_events,
        "next_year_events": next_year_events,
    }
    return render(request, "calendarapp/calendar.html", context)
