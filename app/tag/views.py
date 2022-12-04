from rest_framework import viewsets
from core.models import Tag
from tag.serializers import TagSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.openapi import AutoSchema


class CustomSchema(AutoSchema):

    pass


class TagViewSet(viewsets.ModelViewSet):
    schema = CustomSchema()
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        print(instance)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
