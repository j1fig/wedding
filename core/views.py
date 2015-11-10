from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from core.forms import GuestForm


class GuestAdd(FormView):
    form_class = GuestForm
    success_url = reverse_lazy('home:home')
    template_name = 'core/add_guest.html'
