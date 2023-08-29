from django.contrib import admin
import os

# Register your models here.

admin.site.site_header = os.environ.get("SITE_HEADER_ADMIN", 'Admin WiKi')
admin.site.site_title = os.environ.get("SITE_TITLE_ADMIN", 'WiKi')
admin.site.index_title = os.environ.get("INDEX_TITLE_ADMIN", 'Admin WiKi')
