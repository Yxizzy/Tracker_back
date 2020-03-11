# Generated by Django 3.0.3 on 2020-02-25 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=500, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('vendor', models.CharField(blank=True, choices=[('Jumia', 'Jumia'), ('Konga', 'Konga'), ('Yudala', 'Yudala'), ('Ebay', 'Ebay')], max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(blank=True, choices=[('Order Confirmed', 'Order Confirmed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], max_length=50, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tracker')),
            ],
        ),
    ]