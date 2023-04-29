from django.contrib import admin
from django.urls import path
from stream.views import *
from player.views import *
from musicstream import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home_page'),
    path('admin/', admin.site.urls),
    path('login/', login_user, name='login_page'),
    path('stream/', stream, name='streaming_page'),
    path('logout/', logout_user, name='logout_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

