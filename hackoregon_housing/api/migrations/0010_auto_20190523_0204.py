# Generated by Django 2.0.1 on 2019-05-23 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190523_0158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ncdbsample',
            options={},
        ),
        migrations.RemoveField(
            model_name='ncdbsample',
            name='geo_county',
        ),
        migrations.RemoveField(
            model_name='ncdbsample',
            name='geo_fips',
        ),
        migrations.RemoveField(
            model_name='ncdbsample',
            name='geo_state',
        ),
        migrations.RemoveField(
            model_name='ncdbsample',
            name='geo_tract',
        ),
        migrations.AlterModelTable(
            name='ncdbsample',
            table=None,
        ),
    ]
