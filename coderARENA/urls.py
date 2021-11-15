from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('home.urls')),
	path('', include('judge.urls')),
	path('martor/', include('martor.urls')),
    path('admin/', admin.site.urls),
]
