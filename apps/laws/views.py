from django.shortcuts import render
from .models import ExtractiveDocument
from .serializers import ExtractiveDocumentSerializer, ExtractiveDocumentDetailSerializer
from rest_framework import viewsets
from rest_framework import pagination
from rest_framework.decorators import action
from django.db.models import F
from rest_framework.response import Response
from rest_framework import generics


# Create your views here.
class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 10


# class ExtractiveDocumentViewSet(viewsets.ModelViewSet):
#     queryset = ExtractiveDocument.objects.all()
#     serializer_class = ExtractiveDocumentSerializer
#     pagination_class = CustomPagination
# 
# 
#     @action(detail=False, methods=['get'], url_path='current', url_name='get_current')
#     def getCurrentIssuedDocument(self, request):
#         current_documents = ExtractiveDocument.objects.all().order_by(F('enforced_date').desc(nulls_last = True))[:5]
#         serializer = self.get_serializer(current_documents, many=True)
# 
#         return Response(serializer.data)
# 
#     @action(detail=False, methods=['get'], url_path='upcoming', url_name='get_upcoming')
#     def getUpcomingEffectiveDocument(self, request):
#         upcoming_documents = ExtractiveDocument.objects.all().order_by(F('effective_date').desc(nulls_last = True))[:5]
#         serializer = self.get_serializer(upcoming_documents, many=True)
# 
#         return Response(serializer.data)
# 
#     @action(detail=True, methods=['get'], url_path='upcoming', url_name='get_upcoming_detail')
#     def retrieveCurrentDocument(self, request, pk=None):
#         detail = ExtractiveDocument.objects.filter(id=pk)
#         serializer = ExtractiveDocumentDetailSerializer(detail, many=True)
#         return Response(serializer.data)
# 
#     @action(detail=True, methods=['get'], url_path='current', url_name='get_current_detail')
#     def retrieveCurrentDocument(self, request, pk=None):
#         detail = ExtractiveDocument.objects.filter(id=pk)
#         serializer = ExtractiveDocumentDetailSerializer(detail, many=True)
#         return Response(serializer.data)

class ExtractiveDocumentList(generics.ListAPIView):
    queryset = ExtractiveDocument.objects.all()[:5]
    serializer_class = ExtractiveDocumentSerializer


class ExtractiveDocumentDetail(generics.RetrieveAPIView):
    queryset = ExtractiveDocument.objects.all()
    serializer_class = ExtractiveDocumentDetailSerializer
