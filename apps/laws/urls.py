from django.conf.urls import url, include
from .views import ExtractiveDocumentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'law', ExtractiveDocumentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
