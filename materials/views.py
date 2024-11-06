from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from materials.models import Courses, Lessons
from materials.serializers import CoursesSerializer, LessonsSerializer


class CoursesViewSet(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class LessonsCreateApiView(CreateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsListAPIView(ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsRetrieveAPIView(RetrieveAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsUpdateAPIView(UpdateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsDestroyAPIView(DestroyAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
