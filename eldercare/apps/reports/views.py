from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User

def demo_report_text(request, user_id:int):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return HttpResponseBadRequest("User not found")
    content = f"""Weekly Report for {user.username}
- Adherence charts would be here.
- Use WeasyPrint/ReportLab to render a PDF in production.
"""
    return HttpResponse(content, content_type="text/plain")
