from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User Management
    path('accounts/', include('allauth.urls')), 

    # Local apps
    path('', include('pages.urls')),
    path('books/', include('booksapp.urls')),
    
]


if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls))),
