from django.shortcuts import render

from .models import Groups, SwitchDevices

def index(requiest):
    groups = Groups.objects.all()
    devices = SwitchDevices.objects.all()
    return render(requiest, 'dashboard/index.html', {
        'device': devices,
        'groups': groups,
    })
