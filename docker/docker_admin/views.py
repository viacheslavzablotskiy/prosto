from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework import generics, viewsets, mixins
from .models import Women, Category, Comment, Like, Otvet
from .serializers import WomenSerializer, CommentSerializer, LikeSerializer, OtvetSerializer
from django.shortcuts import HttpResponse
from .tasks import send_feedback_email_task
# from docker_admin.forms import FeedbackForm
# from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


def index_views(request=None):
    send_feedback_email_task.delay()
    return HttpResponse('rghurghiurhoe')

# class FeedbackFormView(FormView):
#     # template_name = "feedback/feedback.html"
#     form_class = FeedbackForm
#     success_url = "/success/"
#
#     def form_valid(self, form):
#         form.send_email()
#         return super().form_valid(form)

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)


class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)


class CommentList(generics.ListCreateAPIView):
    index_views()
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class UserBook(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class UserBookL(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class Otvet_root(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Otvet.objects.all()
    serializer_class = OtvetSerializer


class Otvet_coll(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Otvet.objects.all()
    serializer_class = OtvetSerializer
