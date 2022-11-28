
from django.contrib import admin
from django.urls import path
from docker_admin.views import CommentList

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", CommentList.as_view()),
]
