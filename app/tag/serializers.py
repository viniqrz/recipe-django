from rest_framework.serializers import ModelSerializer, BooleanField
from core.models import Tag


class TagSerializer(ModelSerializer):
    is_draft = BooleanField(write_only=True)

    class Meta:
        model = Tag
        fields = ['id', 'name', 'is_draft', 'status']
        read_only_fields = ['id', 'status']

    def create(self, validated_data):
        if (validated_data['is_draft']):
            validated_data['status'] = 'draft'
        else:
            validated_data['status'] = 'active'
        del validated_data['is_draft']
        return Tag.objects.create(**validated_data)
# class CreateTagSerializer
