from django.http import HttpResponse

def home(request):
    return HttpResponse("Eldercare AI is running.")
