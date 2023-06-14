from django.urls import path
from . import views


urlpatterns = [
    path("", views.SongReviewList.as_view()),
    path("<int:pk>/", views.SongReviewDetail.as_view()),
    path("song-review/<int:post_pk>/comments/", views.SongReviewCommentList.as_view()),
    path("song-review/comment/<int:pk>/", views.SongReviewCommentDetail.as_view()),
]
