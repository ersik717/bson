# Generated by Django 2.2.12 on 2020-06-03 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0022_auto_20200603_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='iin',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
