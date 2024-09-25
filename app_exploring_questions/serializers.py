from rest_framework import serializers

from app_exploring_questions.models import Article, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'color']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'tags', 'image', 'created_at', 'updated_at']
        read_only_fields = ['author']

    tags = TagSerializer(many=True, required=False)

    @staticmethod
    def _set_tags(article, tags_data):
        if tags_data:
            tags_id = []
            for tag_data in tags_data:
                tag_name = tag_data.get('name')
                tag_color = tag_data.get('color', '#FFFFFF')
                tag_obj, created = Tag.objects.get_or_create(name=tag_name, color=tag_color)
                tags_id.append(tag_obj.id)
            article.tags.set(tags_id)

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', None)
        article = super().create(validated_data)

        self._set_tags(article, tags_data)
        return article

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        article = super().update(instance, validated_data) if instance else super().create(validated_data)

        self._set_tags(article, tags_data)
        return article
