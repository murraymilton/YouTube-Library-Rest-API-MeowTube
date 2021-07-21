from django.http import Http404
from django.shortcuts import render
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CommentList(APIView):

    def get(self, request):
        comment = Comment.object.all()
        serializer =CommentSerializer(comment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ModifyComment(APIView):

    def get_by_id(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNOtExist:
            raise Http404

    def get(self, request, pk):
        comment_id = self.get_by_id(pk)
        serializer = CommentSerializer(comment_id)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        comment_id = self.get_by_id(pk)
        comment_id.like += 1
        serializer = CommentSerializer(comment_id, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def post(self, request, pk):
    #     comment_id = self.get_by_id(pk)
    #     serializer = CommentSerializer(comment_id, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=)

    def delete(self, request, pk):
        comment_id = Comment.objects.filter(pk)
        serializer = CommentSerializer(comment_id, pk)
        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, pk):
        comment = Comment.objects.filter(pk)
        serializer = CommentSerializer(comment, pk)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_302_FOUND)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


