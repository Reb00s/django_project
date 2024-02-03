from django.http import HttpResponse


def system_list(request):
    return HttpResponse("Hello from Systems list")


def system_card(request):
    return HttpResponse("Hello from Systems card")