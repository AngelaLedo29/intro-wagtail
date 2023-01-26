from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import InlinePanel


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
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class HomeGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        #FieldPanel('image'),
        FieldPanel('caption'),
    ]