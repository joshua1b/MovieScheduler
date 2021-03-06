from __future__ import unicode_literals

from django.db import models


# Create your models here.
class BroadcastCompany(models.Model):
    """Information of broadcast company"""

    bc_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.bc_name


class MovieSchedule(models.Model):
    """Movie schedule from a cable movie channel"""

    broadcast_company = models.ForeignKey('BroadcastCompany', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    ratings = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.broadcast_company) + " / " + str(self.title)


class LatestUpdate(models.Model):
    """Save last update date for a cable movie channel"""

    broadcast_company = models.ForeignKey('BroadcastCompany', on_delete=models.CASCADE)
    latest_update = models.DateTimeField(null=True)
