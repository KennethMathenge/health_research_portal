# Generated by Django 3.0.3 on 2020-03-17 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("researches", "0009_auto_20200317_0821"),
    ]

    operations = [
        migrations.RemoveField(model_name="research", name="recommends",),
    ]
