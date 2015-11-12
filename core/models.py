from django.db import models


class Guest(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    baby_menu = models.BooleanField(default=False)
    baby_chair = models.BooleanField(default=False)

    diet_restrictions = models.CharField(max_length=255,
                                         blank=True,
                                         null=True)

    # lactose intolerant
    # vegetarian
    # vegan
    # gluten intolerant
    # other
