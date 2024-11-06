from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import CoursesViewSet, LessonsListAPIView, LessonsRetrieveAPIView, LessonsDestroyAPIView, \
    LessonsUpdateAPIView, LessonsCreateApiView

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CoursesViewSet)


urlpatterns = [
    path('materials/', LessonsListAPIView.as_view(), name='materials_list'),
    path('materials/<int:pk>/', LessonsRetrieveAPIView.as_view(), name='materials_retrieve'),
    path('materials/<int:pk>/update/', LessonsUpdateAPIView.as_view(), name='materials_update'),
    path('materials/create/', LessonsCreateApiView.as_view(), name='materials_create'),
    path('materials/<int:pk>/destroy/', LessonsDestroyAPIView.as_view(), name='materials_destroy'),
    ]
