# Generated by Django 2.2.6 on 2019-10-22 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smart_link', models.CharField(max_length=255, verbose_name='Smart Link')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smartlinks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('invoice_id', models.IntegerField(verbose_name='Invoice ID')),
                ('type', models.CharField(choices=[('regular', 'Regular'), ('commercial', 'Commercial'), ('progress', 'Progress')], default='regular', max_length=32, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Amount')),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='paid', max_length=16, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Earnings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date')),
                ('hits', models.IntegerField(default=0, verbose_name='Hits')),
                ('leads', models.IntegerField(default=0, verbose_name='Leads')),
                ('money', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Money')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='earnings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
