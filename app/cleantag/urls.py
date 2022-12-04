from django.urls import path
from cleantag.views import ListTagApi

app_name = 'cleantag'

urlpatterns = [
    path('', ListTagApi.as_view(), name='list')
]
