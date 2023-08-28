"""
URL configuration for wiki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from wiki.plugins.attachments.urls import urlpatterns as attachments_url
from django.urls import re_path
from convert_to_md.views import NewAttachmentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/', include('django_nyt.urls')),
    path('', include('wiki.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

attachments_url.pop(0)
attachments_url += [re_path(r"^$", NewAttachmentView.as_view(),
                            name="attachments_index"),]
print('После изменения')
print(attachments_url)
