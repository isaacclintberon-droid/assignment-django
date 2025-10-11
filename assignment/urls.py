from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('announcements/', include('announcements.urls')),
    path('library/', include('library.urls')),
]
