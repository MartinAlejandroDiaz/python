from django.contrib import admin
from django.urls import path
from perfiles.views import SignUpView, BienvenidaView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
]