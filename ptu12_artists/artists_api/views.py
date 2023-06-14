from django.utils.translation import gettext_lazy as _
from rest_framework import generics, permissions
from . import models, serializers
from rest_framework.exceptions import ValidationError



class SongReviewList(generics.ListCreateAPIView):
    queryset = models.SongReview.objects.all()
    serializer_class = serializers.SongReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class SongReviewCommentList(generics.ListCreateAPIView):
#     queryset = models.SongReviewComment.objects.all()
#     serializer_class = serializers.SongReviewCommentSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class SongReviewLikeList(generics.ListCreateAPIView):
#     queryset = models.SongReviewLike.objects.all()
#     serializer_class = serializers.SongReviewLikeSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class SongReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SongReview.objects.all()
    serializer_class = serializers.SongReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        post = models.SongReview.objects.filter(pk=kwargs["pk"], user=request.user)
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_("You have no rights to update this."))
        
    def delete(self, request, *args, **kwargs):
        post = models.SongReview.objects.filter(pk=kwargs["pk"], user=request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_("You have no rights to delete this."))


class SongReviewCommentList(generics.ListCreateAPIView):
    # queryset = models.SongReviewComment.objects.all()
    serializer_class = serializers.SongReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        song_review = models.SongReview.objects.get(pk=self.kwargs["post_pk"])
        serializer.save(user=self.request.user, song_review=song_review)

    def get_queryset(self):
        song_review = models.SongReview.objects.get(pk=self.kwargs["post_pk"])
        return models.SongReviewComment.objects.filter(song_review=song_review)


class SongReviewCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SongReviewComment.objects.all()
    serializer_class = serializers.SongReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        try:
            comment = models.SongReviewComment.objects.get(pk=kwargs["pk"], user=request.user)
        except Exception as e:
            raise ValidationError(_(f"You cannot update this. Error: {e}"))
        else:
            return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        try:
            comment = models.SongReviewComment.objects.get(pk=kwargs["pk"], user=request.user)
        except Exception as e:
            raise ValidationError(_(f"You cannot delete this. Error: {e}"))
        else:
            return self.destroy(request, *args, **kwargs)
