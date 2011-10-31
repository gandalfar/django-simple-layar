from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    location = models.PointField()
    image = models.ImageField(upload_to="uploads", max_length=256, null=True, blank=True)

    objects = models.GeoManager()

    def __unicode__(self): return self.name