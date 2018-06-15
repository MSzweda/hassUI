from django.urls import reverse
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'dashboard/index.html'
