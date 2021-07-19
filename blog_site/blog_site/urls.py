
from django.urls.conf import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('articles/',include('articles.urls')),
    path('accounts/', include('accounts.urls'))
]
