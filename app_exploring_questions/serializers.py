from rest_framework import serializers

from app_exploring_questions.models import Article, Tag


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['author']

    def create(self, validated_data):
        tags = validated_data.pop('tags', None)
        article = super().create(validated_data)
        tags_id = []
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(name=tag)
            tags_id.append(tag_obj.id)
        article.tags.set(tags_id)

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)
        article = super().update(instance, validated_data) if instance else super().create(validated_data)
        tags_id = []
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(name=tag)
            tags_id.append(tag_obj.id)
        article.tags.set(tags_id)
