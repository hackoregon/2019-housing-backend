# Generated by Django 2.2.2 on 2019-06-30 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_totalloans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hmdaorwa',
            name='index',
            field=models.BigIntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='totalloans',
            name='index',
            field=models.BigIntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
