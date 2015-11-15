from django.views.generic import TemplateView

from core.models import Accomodation


class Home(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(Home, self).get_context_data(*args, **kwargs)
        ctx['accomodations'] = Accomodation.objects.all()
        return ctx
