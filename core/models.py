from django.db import models


class Accomodation(models.Model):
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class Room(models.Model):
    accomodation = models.ForeignKey(Accomodation)


class Bed(models.Model):
    DOUBLE = 'double'
    SINGLE = 'single'
    BED_CHOICES = (
        (DOUBLE, 'do'),
        (SINGLE, 'si'),
    )
    type = models.CharField(max_length=2,
                            choices=BED_CHOICES,
                            default=SINGLE)
    is_sofa_bed = models.BooleanField(default=False)
    room = models.ForeignKey(Room)


class Guest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    baby_menu = models.BooleanField(default=False)
    baby_chair = models.BooleanField(default=False)

    diet_restrictions = models.CharField(max_length=255,
                                         blank=True,
                                         null=True)

    bed = models.ForeignKey(Bed,
                            null=True,
                            blank=True,
                            on_delete=models.SET_NULL)

    # lactose intolerant
    # vegetarian
    # vegan
    # gluten intolerant
    # other
