# Generated by Django 2.1.7 on 2019-07-02 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_environmentlogin_logintype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='environmentlogin',
            name='loginType',
        ),
        migrations.RemoveField(
            model_name='loginconfig',
            name='loginType',
        ),
    ]
