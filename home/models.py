from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    '''
    Añadimos campo *body* de texto enriquecido
    '''
    # Subapage de la aplicación blog
    #sugpage_types = ['blog.BlogIndexPage']

    # No permito que tenga nuevas subpáginas
    #sugpage_types = []
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]