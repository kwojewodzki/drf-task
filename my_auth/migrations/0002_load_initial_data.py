# Generated by Django 4.2.5 on 2023-10-10 13:32

from django.db import migrations
import os
from sys import path
from django.core import serializers

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'initial_data.json'

def load_fixture(apps, schema_editor):
    fixture_file = os.path.join(fixture_dir, fixture_filename)

    fixture = open(fixture_file, 'rb')
    objects = serializers.deserialize('json', fixture, ignorenonexistent=True)
    for obj in objects:
        obj.save()
    fixture.close()

class Migration(migrations.Migration):

    dependencies = [
        ('my_auth', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture)
    ]
