from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('page/', include('pages.urls')),
    path('services/', include('services.urls')),
    path('contact/', include("contact.urls")),
]

# aca mapeamos archivos estaticos si estamos debuggeando 

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Extendemos la cfg del panel de admin

admin.site.site_header = "La Caffettiera"
admin.site.index_title = "Panel de Administrador"
admin.site.site_title = "La Caffetiera"
