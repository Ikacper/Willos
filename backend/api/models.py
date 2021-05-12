from django.contrib.gis.db import models


class Property(models.Model):
    class PropertyTypes(models.TextChoices):
        DETACHED = "DETACHED", "Detached house"
        SEMIDETACHED = "SEMIDETACHED", "Semi-detached house"
        TERRACED = "TERRACED", "Terraced house"
        BUNGALOW = "BUNGALOW", "Bungalow"
        DETACHEDBUNGALOW = "DETACHEDBUNGALOW", "Detached bungalow"
        SEMIDETACHEDBUNGALOW = "SEMIDETACHEDBUNGALOW", "Semi-detached bungalow"
        TERRACEDBUNGALOW = "TERRACEDBUNGALOW", "Terraced bungalow"
        COTTAGE = "COTTAGE", "Cottage"
        MOBILEPARK = "MOBILEPARK", "Mobile/park home"
        FLAT = "FLAT", "Flat"
        LAND = "LAND", "Land"
        PARKHOME = "PARKHOME", "Park home"

    url = models.URLField(null=True)
    thumbnail = models.URLField(null=True)
    title = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    date = models.DateField(null=True)
    agent_name = models.CharField(max_length=50, null=True)
    agent_phone = models.CharField(max_length=50, null=True)
    agent_address = models.CharField(max_length=100, null=True)
    property_type = models.CharField(
        max_length=25, choices=PropertyTypes.choices, null=True
    )
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)
    receptionrooms = models.IntegerField(null=True)
    sqft = models.CharField(max_length=15, null=True)
    description = models.TextField(null=True)
    key_features = models.JSONField(null=True)
    stations = models.JSONField(null=True)
    listing_history = models.JSONField(null=True)
    cordinates = models.PointField(null=True)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
