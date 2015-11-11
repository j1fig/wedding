from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from django.http import JsonResponse

from core.forms import GuestForm


class GuestAdd(FormView):
    form_class = GuestForm
    success_url = reverse_lazy('home:home')
    template_name = 'core/add_guest.html'

    def form_valid(self, form):
        form.save()
        context = {
            'next': self.get_success_url(),
            'success': True
        }
        return JsonResponse(context)

    def form_invalid(self, form):
        response = self.render_to_response(self.get_context_data(form=form))
        form_html = response.render().content
        return JsonResponse({'success': False, 'form_html': form_html})
