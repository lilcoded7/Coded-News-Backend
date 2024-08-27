from django.urls import path, include
from news.views import *

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("blog/news", BlogNewViewSet),


urlpatterns = [
    path("", include(router.urls)),
    path('list/news/category/<str:category_id>', BlogNewsCategory.as_view(), name='list_news_category')
]