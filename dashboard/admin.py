from django.contrib import admin

from .models import Groups, SwitchDevices


class GroupsAdmin(admin.ModelAdmin):
    list_display = ('group_name', )


class SwitchDevicesAdmin(admin.ModelAdmin):
    list_display = ('actual_name', 'ip_address', 'group', 'location', 'state_now')


admin.site.register(Groups, GroupsAdmin)
admin.site.register(SwitchDevices, SwitchDevicesAdmin)
