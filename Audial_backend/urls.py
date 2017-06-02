"""Audial_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from apps.restapi.models import User, Track
from rest_framework import routers, serializers, viewsets, generics

class TrackSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Track
		fields = ('id','name','artist','spotify_id','uri')

class FollowingSerializer(serializers.HyperlinkedModelSerializer):
	active_track = TrackSerializer()
	class Meta:
		model = User
		fields = ('id','display_name','spotify_id','active_track')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('id','display_name','spotify_id','following','active_track')

	def to_representation(self, instance):
		representation = super(UserSerializer, self).to_representation(instance)
		# print(FollowingSerializer(instance.following.all(), many=True).data)
		representation['following'] = FollowingSerializer(instance.following.all(), many=True).data
		representation['active_track'] = TrackSerializer(instance.active_track).data
		return representation

	def update(self,instance, validated_data):
		if validated_data['active_track'] is not None:
			instance.active_track = validated_data['active_track']
		if validated_data['following']:
			instance.following.add(validated_data['following'][0])
		instance.save()
		return instance

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def get_queryset(self):
		queryset = User.objects.all()
		spotify_id = self.request.query_params.get('spotify_id', None)
		if spotify_id is not None:
			queryset = queryset.filter(spotify_id=spotify_id)
		return queryset


class TrackViewSet(viewsets.ModelViewSet):
	queryset = Track.objects.all()
	serializer_class = TrackSerializer

	def get_queryset(self):
		queryset = Track.objects.all()
		spotify_id = self.request.query_params.get('spotify_id', None)
		if spotify_id is not None:
			queryset = queryset.filter(spotify_id=spotify_id)
		return queryset

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tracks', TrackViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^token/', include('apps.restapi.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
]
