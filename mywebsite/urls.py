from django.contrib import admin
from django.urls import path, include

app_name = "sosmed"

urlpatterns = [
	path('sosmed/', include('sosmed.urls'), name='sosmed'),
    path('admin/', admin.site.urls),
]
