# Generated by Django 5.2.1 on 2025-06-09 10:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20250609_1535'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст жалобы')),
                ('complaining_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL, verbose_name='Кто пожаловался')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='property.flat', verbose_name='Квартира, на которую пожаловались')),
            ],
        ),
    ]
