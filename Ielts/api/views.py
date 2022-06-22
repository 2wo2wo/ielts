from django.http import Http404
from django.shortcuts import render
from .models import (
    MatchingHeadingCollection,    MatchingHeadingChoices,     MatchingHeadingText,
    TrueFalse,    ParagraphMatching,     Part,     GivenKey,    SummaryCompletion,
    SentencePart, MultipleChoice,List, WholeList, ListSection,
    TableChoices, TablePart, TableCompletion , ChoicePart , MatchingSentence,
    GivenPart, FlowChart, FlowChartAnswer,Book

)
from rest_framework.generics import CreateAPIView
from .serializers import MatchingCollectionSerializer , BookSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



class MatchingCollectionView(ModelViewSet):
    queryset = MatchingHeadingCollection.objects.all()
    serializer_class = MatchingCollectionSerializer

class CollectionView(APIView):
    # def get_object(self, request, pk, format=None):


    def get(self, request,pk,format=None):
        collections = MatchingHeadingCollection.objects.all()[pk-1]
        serializer = MatchingCollectionSerializer(collections)
        return Response(serializer.data)





# class BookView(APIView):
#
#
#     def get_passage(self, pk , order):
#         try:
#             object = self.get_object(pk)
#         except passage
#
#
#     def get_book(self, pk):
#         try:
#             return self.get_passage()
#         except Book.DoesNotExist:
#             raise Http404
#
#
#
#     def get_answers(self, ):
#         pass
#
#     def get(self, request, pk, format=None):
#         books = Book.objects.all()[pk - 1]
#         serializer = BookSerializer(books)
#         return Response(serializer.data)
#
#
#     def post(self, request, pk , format=None):
#
#         answers = {
#             "text_paragraph" : '1'
#         }
#         return Response()
