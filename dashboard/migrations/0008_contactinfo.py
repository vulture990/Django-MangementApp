# Generated by Django 2.2.6 on 2019-10-24 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0007_auto_20191023_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='address')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='email address')),
                ('phone_number', models.CharField(blank=True, max_length=60, null=True, verbose_name='phone number')),
                ('website', models.CharField(blank=True, max_length=255, null=True, verbose_name='website')),
                ('skype', models.CharField(blank=True, max_length=255, null=True, verbose_name='skype')),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True, verbose_name='linkedin')),
                ('instagram', models.CharField(blank=True, max_length=255, null=True, verbose_name='instagram')),
                ('twitter', models.CharField(blank=True, max_length=255, null=True, verbose_name='twitter')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True, verbose_name='facebook')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
