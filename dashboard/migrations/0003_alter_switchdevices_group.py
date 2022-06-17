# Generated by Django 4.0.5 on 2022-06-17 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_switchdevices_state_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='switchdevices',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dashboard.groups', verbose_name='Group'),
        ),
    ]