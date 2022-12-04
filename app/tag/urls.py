from django.urls import path, include
from tag.views import TagViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('', TagViewSet)

app_name = 'tag'

urlpatterns = [
    path('', include(router.urls))
]
