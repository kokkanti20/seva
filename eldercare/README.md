# Eldercare AI (Free-Only MVP)

A lightweight Django + DRF project for an AI-assisted elder care calendar & reminder app using only free/open-source components.

## Features
- Medications: CRUD for meds, schedules, and events
- Appointments & routines: Calendar entries
- Assistant stubs for local ASR/TTS (Whisper/Coqui) and local intent parsing
- SOS via console email backend
- Weekly reports (placeholder service)
- Celery stubs for reminders (optional)

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Create DB
python manage.py migrate
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## API (Partial)
- `/api/meds/` (Medication)
- `/api/medschedules/` (MedSchedule)
- `/api/medevents/` (MedEvent)
- `/api/appointments/` (Appointment)
- `/api/routines/` (Routine)
- `/assistant/parse_med/` (demo prescription parser)
- `/assistant/weekly_summary/<user_id>/` (demo text summary)

> Note: This is an MVP scaffold meant for coursework. Replace the assistant stubs with your local Whisper/Coqui/HF pipelines when ready.
