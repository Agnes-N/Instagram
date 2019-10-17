from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^new/upload$', views.new_image, name='upload'),
    url(r'^new/profile$', views.new_profile, name='profile'),
  
    # url(r'^tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    