from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^caffe/', include('caffe_app.urls')),
    url(r'^tensorflow/', include('tensorflow_app.urls')),
    url(r'^keras/', include('keras_app.urls')),
    url(r'^admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
