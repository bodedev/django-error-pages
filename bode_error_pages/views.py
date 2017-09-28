# -*- coding: utf-8 -*-


from django.views.generic.base import TemplateView


class Error403View(TemplateView):

    template_name = 'website/errors/403.html'


class Error404View(TemplateView):

    template_name = 'website/errors/404.html'


class Error500View(TemplateView):

    template_name = 'website/errors/500.html'
