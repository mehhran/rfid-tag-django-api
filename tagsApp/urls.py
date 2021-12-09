from tagsApp.views import TagsAPIView
from django.urls import path

urlpatterns = [
    path("", TagsAPIView.as_view() , name="tags"),
]
