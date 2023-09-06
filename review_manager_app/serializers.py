from rest_framework import serializers
from .models import Review, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='name',
        required=False,
    )

    class Meta:
        model = Review
        fields = '__all__'

class CaseInsensitiveChoiceField(serializers.ChoiceField):
    def to_internal_value(self, data):
        data = data.lower()
        return super().to_internal_value(data)

class AddRemoveTagSerializer(serializers.Serializer):
    ACTION_CHOICES = [
        ('add', 'Add'),
        ('remove', 'Remove'),
    ]
    review_id = serializers.IntegerField()
    tag_names = serializers.ListField(child=serializers.CharField())
    action = CaseInsensitiveChoiceField(choices=ACTION_CHOICES)
