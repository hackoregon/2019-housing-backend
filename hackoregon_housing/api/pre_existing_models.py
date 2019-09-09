from django.contrib.gis.db import models


class PortlandHomeOwnershipByRace(models.Model):
    yr = models.FloatField(blank=True, null=True)
    race = models.TextField(blank=True, null=True)
    home_ownership_rate = models.FloatField(blank=True, null=True)
    home_ownership_count = models.FloatField(blank=True, null=True)
    household_count = models.FloatField(blank=True, null=True)
    geoname = models.TextField(blank=True, null=True)
    fips = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portland_home_ownership_by_race'
