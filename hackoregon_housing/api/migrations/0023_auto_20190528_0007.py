# Generated by Django 2.0.1 on 2019-05-28 00:07

from django.db import migrations

def add_fips_foreign_key_changes(apps, schema_editor):
    NcdbSampleChanges = apps.get_model("api", "NcdbSampleChanges")
    fips = apps.get_model("api", "FIPSRecords")
    for fipsinstance in fips.objects.all():
        for changesinstance in NcdbSampleChanges.objects.all().filter(geo_fips=fipsinstance.geo_fips):
            changesinstance.fips_code = fipsinstance
            changesinstance.save()

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_ncdbsamplechanges_fips_code'),
    ]

    operations = [
        migrations.RunPython(add_fips_foreign_key_changes)
    ]
