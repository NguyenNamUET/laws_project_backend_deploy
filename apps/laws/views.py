from django.shortcuts import render
from .models import ExtractiveDocument
from .serializers import ExtractiveDocumentSerializer
from rest_framework import viewsets
from rest_framework import pagination
from rest_framework.decorators import action
from django.db.models import F

# Create your views here.
class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 10


class ExtractiveDocumentViewSet(viewsets.ModelViewSet):
    queryset = ExtractiveDocument.objects.all()
    serializer_class = ExtractiveDocumentSerializer
    pagination_class = CustomPagination

    #Các router tồn tại:
    #law/ mặc định của ModelViewSet
    #law/{pk}/ mặc định của ModelViewSet
    #law/current/ của def getCurrentIssuedDocument
    #law/upcoming/ của def getUpcomingEffectiveDocumnet

    @action(detail=False, methods=['get'], url_path='current', url_name='get_current')
    def getCurrentIssuedDocument(self, request):
        current_document = ExtractiveDocument.objects.order_by(F('enforced_date').desc(nulls_last = True))[:100]
        ##Note: Rerun migration && Change to issued_date
        page = self.paginate_queryset(current_document)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    @action(detail=False, methods=['get'], url_path='upcoming', url_name='get_upcoming')
    def getUpcomingEffectiveDocumnet(self, request):
        upcoming_document = ExtractiveDocument.objects.order_by(F('effective_date').desc(nulls_last = True))[:100]
        page = self.paginate_queryset(upcoming_document)
        serializer = self.get_serializer(page, many=True)

        return self.get_paginated_response(serializer.data)

    # @action(detail=False, methods=['get'], url_path='upcoming', url_name='get_upcoming')
    # def getBoth(self, request):