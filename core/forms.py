from django.forms import ModelForm

from .models import Guest


class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = (
            'first_name',
            'last_name',
            'baby_menu',
            'baby_chair',
            'diet_restrictions',
        )
