# Generated by Django 3.2 on 2023-02-15 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agriculture', '0002_culture_farmer_plot_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='user_name',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
