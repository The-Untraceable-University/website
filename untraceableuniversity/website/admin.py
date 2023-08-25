from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    # Text to put at the end of each page"s <title>.
    site_title = "Untraceable University Admin"

    # Text to put in each page"s <h1> (and above login form).
    site_header = "Untraceable University Admin"

    # Text to put at the top of the admin index page.
    index_title = "Untraceable University"
    enable_nav_sidebar = False

admin_site = MyAdminSite()

admin_site.register(Language)
admin_site.register(Page)
admin_site.register(PageContent)
admin_site.register(Inspiration)
