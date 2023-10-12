# Generated by Django 4.2.5 on 2023-10-12 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import thumbnail_api.models
import thumbnail_api.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to=thumbnail_api.models.upload_to)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExpiringLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=256)),
                ('time_to_expire', models.IntegerField(validators=[thumbnail_api.validators.validate_time_to_expire])),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='thumbnail_api.image')),
            ],
        ),
    ]
