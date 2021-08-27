"""
Definition of urls for ginkgo.
"""

from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('notice/', include('notice.urls')),
    path('article/', include('article.urls')),
    path('propaganda/', include('propaganda.urls')),
    path('', include('basic.urls')),
    path('basic/', include('basic.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)