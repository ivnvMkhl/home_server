from django.shortcuts import render

from .models import Groups, SwitchDevice

def index(requiest):
    groups = Groups.objects.all()
    devices = SwitchDevice.objects.all()
    return render(requiest, 'dashboard/index.html', {
        'device': devices,
        'groups': groups,
    })
