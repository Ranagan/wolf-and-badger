from allauth.account.decorators import login_required
from django.shortcuts import render


def profile(request):
    return render(request, "profile.html", {})
