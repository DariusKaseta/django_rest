from rest_framework import serializers
from . import models

class SongReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    user_id = serializers.ReadOnlyField(source="user.id")
    song_review = serializers.ReadOnlyField(source="song_review.id")

    class Meta:
        model = models.SongReviewComment
        fields = ["id", "user_id", "user", "song_review", "content"]


class SongReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    user_id = serializers.ReadOnlyField(source="user.id")
    class Meta:
        model = models.SongReview
        fields = ["id", "user_id", "user", "song", "content", "score"]


# class SongReviewCommentSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source="user.username")
#     user_id = serializers.ReadOnlyField(source="user.id")
#     class Meta:
#         model = models.SongReviewComment
#         fields = ["id", "user_id", "user","song_review", "content"]


# class SongReviewLikeSerializer(serializers.ModelSerializer):
#     user = serializers.ReadOnlyField(source="user.username")
#     user_id = serializers.ReadOnlyField(source="user.id")
#     class Meta:
#         model = models.SongReviewLike
#         fields = ["id", "user_id", "user", "song_review"]