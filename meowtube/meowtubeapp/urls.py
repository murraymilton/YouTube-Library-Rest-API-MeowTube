from django.urls import path
from . import views

urlpatterns = [
    path('comment/', views.CommentList.as_view()),
    path('comment<int:pk>/', views.ModifyComment.as_view())
]