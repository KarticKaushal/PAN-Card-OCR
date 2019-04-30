from django.conf.urls import url 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.first_view, name='first_view'),
    url(r'^uimage/$', views.uimage, name='uimage'), #image upload template!
    url(r'^pancard/$', views.ocr_core, name='PanCard'), #PAN Card OCR template!
   

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

