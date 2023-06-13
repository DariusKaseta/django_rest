from rest_framework import serializers
from . import models

class SongReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    user_id = serializers.ReadOnlyField(source="user.id")
    class Meta:
        model = models.SongReview
        fields = ["id", "user_id", "user", "song", "content", "score"]