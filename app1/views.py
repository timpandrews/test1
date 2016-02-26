from django.shortcuts import render

# Create your views here.
def home(request):

    msg = "Welcome"
    context = {
        "msg": msg,
    }

    return render(request, "home.html", context)

def registration(request):

    msg = "Welcome"
    context = {
        "msg": msg,
    }

    return render(request, "registration.html", context)