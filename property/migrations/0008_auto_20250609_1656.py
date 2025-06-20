# Generated by Django 5.2.1 on 2025-06-09 11:56
import phonenumbers
from django.db import migrations
from django.db.migrations import RunPython


def normalize_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        if flat.owners_phonenumber:
            flat.owner_pure_phone = phonenumbers.parse(flat.phonenumber, 'RU')
            if phonenumbers.is_valid_number(flat.owner_pure_phone):
                flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumbers)
    ]
