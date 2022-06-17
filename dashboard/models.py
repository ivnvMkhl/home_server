from django.db import models


class Groups(models.Model):
    group_name = models.CharField(max_length=30, verbose_name='Group name', db_index=True)

    def __int__(self):
        return self.group_name


    class Meta:
        verbose_name = 'Devices group'
        verbose_name_plural = 'Devices groups'


class SwitchDevices(models.Model):
    actual_name = models.CharField(max_length=30, verbose_name='Device name')
    ip_address = models.URLField(verbose_name='IP address')
    group = models.ForeignKey(Groups, on_delete=models.PROTECT, verbose_name='Group')
    device_type = models.CharField(max_length=30, verbose_name='Type')
    location = models.CharField(max_length=30, verbose_name='Locate', blank=True)
    start_state = models.BooleanField(default=False, verbose_name='Start state')
    created_timestamp = models.DateTimeField(auto_now=True, verbose_name='Created date')
    state_now = models.BooleanField(default=False, verbose_name='Enabled')

    def __int__(self):
        return self.actual_name

    class Meta:
        verbose_name = 'Switch device'
        verbose_name_plural = 'Switch devices'
