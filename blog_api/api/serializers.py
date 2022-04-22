from rest_framework import serializers

from posts.models import Post, Comment


class FilterClass(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        if value.level <= 1:
            serializer = self.parent.parent.__class__(
                value, context=self.context
            )
            return serializer.data


class AllRecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentThredSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)

    class Meta:
        list_serializer_class = FilterClass
        model = Comment
        fields = ("id", "author", "post", "created", "children")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "author", "post", "created")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "author", "text", "pub_date")


class PostWithCommentarySerializer(serializers.ModelSerializer):
    comments = CommentThredSerializer(
        many=True,
        required=False,
    )

    class Meta:
        model = Post
        fields = ("id", "author", "text", "pub_date", "comments")


class GetAllCommentarySerializer(serializers.ModelSerializer):
    children = AllRecursiveField(many=True)

    class Meta:
        model = Comment
        fields = fields = ("id", "author", "post", "created", "children")
