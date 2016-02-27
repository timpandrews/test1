from django.shortcuts import render

from .forms import User_Registartion_Form

# Create your views here.
def home(request):

    msg = "Welcome"
    context = {
        "msg": msg,
    }

    return render(request, "home.html", context)

def registration(request):

    msg = "Welcome"
    show_form = True

    form = User_Registartion_Form(request.POST or None)

    context = {
        "msg": msg,
        "show_form": show_form,
        "form": form,
    }

    if form.is_valid():
        form.save()
        msg = "Thank you for registering!"
        show_form = False
        context = {
            "msg": msg,
            "show_form": show_form,
        }

    return render(request, "registration.html", context)