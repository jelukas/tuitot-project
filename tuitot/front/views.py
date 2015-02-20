from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from allauth.socialaccount.models import SocialAccount, SocialToken


@login_required
def home(request):
    template = 'front/home.html'
    context = {}
    return render(request, template, context)
