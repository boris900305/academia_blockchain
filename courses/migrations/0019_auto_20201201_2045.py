# Generated by Django 3.0.4 on 2020-12-01 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_certificaterequest_accepted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificaterequest',
            name='rejected',
        ),
        migrations.AlterField(
            model_name='certificaterequest',
            name='accepted',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
