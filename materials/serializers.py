from rest_framework.serializers import ModelSerializer

from materials.models import Courses, Lessons


class CoursesSerializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class LessonsSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = '__all__'