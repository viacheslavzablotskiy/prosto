from django.contrib import admin
from django.urls import path, include, re_path
from docker_admin.views import *
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', WomenAPIList.as_view(), name="margo"),
    path('api/<int:pk>/', WomenAPIDetailView.as_view(), name="main"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/', include('djoser.urls')),
    path('comments/', CommentList.as_view(), name='comments'),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('api/like/', UserBook.as_view()),
    path('api/like/<int:pk>/', UserBookL.as_view()),
    path('api/otvet/', Otvet_root.as_view()),
    path('api/otvet/<int:pk>/', Otvet_coll.as_view()),
]