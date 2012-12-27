# -*- coding: utf-8 -*-
"""

Yarım kaldı, arkası yarın

"""


from django.db import models
from django.utils.translation import ugettext_lazy as _


PAGE_TYPES = (
        ('homepage', u'Anasayfa'),
        ('postpage', u'Makale Sayfası'),
        ('all',      u'Tümü'), # diğerlerini pasif yapacak
    )


class SiteDetails(models.Model):
    """
        Site için genel bilgileri ve ayarları içerir
    """
    about = models.TextField(_('Hakkımda'))
    
    enable_comments = models.BooleanField(_('Yorumları aktif et'), default=True)



class Picture(models.Model):
    title = models.CharField(_('Resim Başlığı'), max_length=40)
    picture = models.ImageField()



class Page(models.Model):
    page = models.CharField(_('Sayfa'), max_length=30, choices=PAGE_TYPES)


class SeoSablon(models.Model):
    """
        Seo ayarları için gerekli şablonları tutar
        Template Tag'i ile sayfa tipine göre seo ayarları template'a eklenir
    """
    title = models.CharField(_('Başlık'), max_length=60)
    keywords = models.CharField(_('Anahtar Kelimeler'))
    description = models.CharField(_('Açıklama'))
    
    page = models.ForeignKey(Page, verbose_name=_('Sayfa'))




