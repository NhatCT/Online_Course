from courses.models import Category, Course, Lesson, Tag
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']

class ItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data=super().to_representation(instance)
        data['image']=instance.image.url

        return data
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id','subject','image','created_date','category_id']

class LessonSerializer(ItemSerializer):
    class Meta:
        model=Lesson
        fields=['id','subject','image','created_date']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['id','name']
class LessonDetailsSerializer(LessonSerializer):
    tags=TagSerializer(many=True)
    class Meta:

        model=LessonSerializer.Meta.model
        fields=LessonSerializer.Meta.fields+['content','tags']