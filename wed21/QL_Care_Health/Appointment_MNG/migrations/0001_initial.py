# Generated by Django 5.1.4 on 2025-01-02 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('pet_id', models.IntegerField()),
                ('veterinarian_id', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=50)),
                ('notes', models.TextField()),
            ],
        ),
    ]
