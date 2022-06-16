from django.db import models


class Groups(models.Model):
    group_name = models.CharField(max_length=30, verbose_name='Group name', db_index=True)

    def __int__(self):
        return self.group_name


class SwitchDevice(models.Model):
    actual_name = models.CharField(max_length=30, verbose_name='Device name')
    ip_address = models.URLField(verbose_name='IP address')
    grop = models.ForeignKey(Groups, on_delete=models.PROTECT)
    device_type = models.CharField(max_length=30, verbose_name='Type')
    location = models.CharField(max_length=30, verbose_name='Locate', blank=True)
    start_state = models.BooleanField(default=False, verbose_name='Start state')
    created_timestamp = models.DateTimeField(auto_now=True, verbose_name='Created date')

    def __int__(self):
        return self.actual_name

