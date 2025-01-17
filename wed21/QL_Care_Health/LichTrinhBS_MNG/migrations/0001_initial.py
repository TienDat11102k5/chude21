# Generated by Django 5.1.4 on 2025-01-17 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Veterinarian_MNG', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LichTrinhBS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('note', models.TextField(blank=True, null=True)),
                ('veterinarian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lich_trinh', to='Veterinarian_MNG.veterinarian')),
            ],
        ),
    ]
