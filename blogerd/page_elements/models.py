from django.db import models


#################### MENUS ####################

LOCATIONS = (
        ('header',      'Header'),
        ('footer',    'Footer'),
        ('sideline',  'Sideline'),
    )

class Menu(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    slug = models.SlugField()
    location = models.CharField(max_length=30, choices=LOCATIONS)

    def get_children(self):
        """
            Returns menuitems
        """
        pass

class MenuItem(models.Model):
    name = models.CharField(max_length=40)
    url = models.URLField()
    menu = models.ForeignKey(Menu)

# template tag'i
def get_menu(menu_name):
    pass



#################### LINKS ####################

class LinkedPage(models.Model):
    url = models.URLField()
    ordering = models.CharField(max_length=40)

# related template tag
def get_links():
    LinkedPage.objects.order_by('ordering') # gibi

