# from django.conf.urls import url, include
# from .views import ExtractiveDocumentViewSet, ExpiredDocumentViewSet, UpcomingEffectiveDocumentViewSet
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register(r'laws', ExtractiveDocumentViewSet)
# router.register(r'laws/expiry', ExpiredDocumentViewSet)
# router.register(r'law/upcoming', UpcomingEffectiveDocumentViewSet)
#
# urlpatterns = [
#     url(r'^', include(router.urls)),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('laws/', views.ExtractiveDocumentList.as_view()),
    # path('laws/expiry/', views.ExpiredDocument.as_view()),
    # path('laws/upcoming/', views.UpcomingEffectiveDocument.as_view()),
    path('laws/<int:pk>/', views.ExtractiveDocumentDetail.as_view()),
    # path('laws/expiry/<int:pk>/', views.ExpiredDocumentDetail.as_view()),
    # path('laws/upcoming/<int:pk>/', views.UpcomingEffectiveDocumentDetail.as_view()),
]