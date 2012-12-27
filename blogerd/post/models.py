# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.markup.templatetags import markup
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(_('Etiket ismi'), max_length=25)
    slug = models.SlugField()
    
    class Meta:
        verbose_name = _('Etiket')
        verbose_name_plural = _('Etiketler')
        ordering = ('-name',)
    
    def save(self, *args, **kwargs):
        self.name = self.name.strip().lower()
        # geçici çözüm...kendi slugify'ını olustur
        if not self.slug:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        pass


class PostManager(models.Manager):
    def active_posts(self):
        return self.filter(is_active=True)


class Post(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField()
    
    content = models.TextField(_('content'))
    rendered_content = models.TextField(_('rendered content'), blank=True)
    
    author = models.ForeignKey(User, verbose_name=_('Yazar'))
    
    date_created = models.DateTimeField(_('Oluşturulma tarihi'), default=datetime.now)
    date_modified = models.DateTimeField(_('Son düzenleme tarihi'))
    
    is_active = models.BooleanField(_('aktif mi ?'), default=False)
    
    tags = models.ManyToManyField(Tag, verbose_name=_('tags'), blank=True)
    
    objects = PostManager()
    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ('-created_at',)
    
    def save(self, *args, **kwargs):
        self.last_edited_at = datetime.now()
        self.rendered_content = markup.markdown(self.content)
        super(Post, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        # sonra düzelt
        return "%s" % (self.slug)






