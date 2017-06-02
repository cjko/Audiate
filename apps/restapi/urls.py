from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^swap$', views.swap),
	url(r'^refresh$', views.refresh),
]