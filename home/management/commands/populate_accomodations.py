from optparse import make_option

from django.core.management import BaseCommand

from core.models import Accomodation


def get_accomodations():
    accomodations = [
        {
            'name': "T 57",
            'url': "http://www.t57domus.it/traetta57/"
        },
        {
            'name': "Dimore di Edward",
            'url': "http://www.ledimorediedward.it/"
        },
        {
            'name': "Il Basilisco",
            'url': "http://www.ilbasilisco.com/"
        },
        {
            'name': "Palazzo Santorelli",
            'url': "http://www.palazzosantorelli.it/"
        },
        {
            'name': "Il solito Posto Bnb",
            'url': "www.booking.com/hotel/it/b-amp-b-il-solito-posto.html"
        },
        {
            'name': "Chianca",
            'url': "http://www.booking.com/hotel/it/la-chianca-home.html"
        },
        {
            'name': "Porta Baresana",
            'url': "http://www.portabaresana.it/en/"
        },
        {
            'name': "Vico Storto",
            'url': "http://www.t57domus.it/vicostorto/"
        },
        {
            'name': "Cappuccini",
            'url': ""
        },
        {
            'name': "San Lorenzo",
            'url': "http://www.bebsanlorenzo.it/"
        },
        {
            'name': "Palazzo Sienna de Facendis",
            'url': "https://www.airbnb.com/rooms/5897103"
        },
        {
            'name': "Domus Artis",
            'url': "http://www.booking.com/hotel/it/bed-amp-breakfast.html"
        },
        {
            'name': "Il Cimiero",
            'url': "http://www.ilcimiero.it/"
        },
        {
            'name': "Stanza privata Il Duca di Montemar",
            'url': "https://www.airbnb.com/rooms/5687808"
        }
    ]

    return [Accomodation(name=a['name'], url=a['url']) for a in accomodations]


class Command(BaseCommand):
    """
    A fixture alternative to not overwrite previous entries.
    """
    args = '<app_name>'
    help = 'Populates the accomodation table.'
    option_list = BaseCommand.option_list + (
        make_option(
            '--delete',
            action='store_true',
            dest='delete',
            default=False,
            help='Delete all accomodation table entries.'
        ),
    )

    def handle(self, *args, **options):
        accomodations = get_accomodations()
        if options['delete']:
            Accomodation.objects\
                .filter(name__in=[a.name for a in accomodations])\
                .delete()
        else:
            Accomodation.objects.bulk_create(accomodations)
