from django.shortcuts import render
from .models import Installer
from django.contrib.auth.decorators import login_required

@login_required
def main_page(request):
    installers = Installer.objects.all().order_by('Name')
    return render(request, 'main.html', {'installers':installers})
# Create your views here.
