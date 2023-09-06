from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'reviews', views.ReviewViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/add-remove-tag', views.AddRemoveTag.as_view(), name='add-tag-to-review')
]
