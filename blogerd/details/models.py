# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class SiteDetails(models.Model):
    about_me = models.TextField(_('Hakkımda'))


class SeoSablon(models.Model):
    site_title = models.CharField(_('Site Başlığı'), max_length=60)