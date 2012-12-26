# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.contrib.markup.templatetags import markup


class Tag(models.Model):
    pass


class PostManager(models.Manager):
    pass


class Post(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField()
    
    content = models.TextField(_('content'))
    rendered_content = models.TextField(_('rendered content'), blank=True)
    
    author = models.ForeignKey(User, verbose_name=_('Yazar'))
    
    created_at = models.DateTimeField(default=datetime.now)
    last_edited_at = models.DateTimeField()
    
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
        return "%s" % (self.slug)






