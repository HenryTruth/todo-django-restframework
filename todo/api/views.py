import json
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from todo.models import Todos
from .serializers import TodosSerializer

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

class TodosAPIDetailView(mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.RetrieveAPIView):
    serializer_class = TodosSerializer
    queryset = Todos.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_destroy(self,instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None



class TodosAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = TodosSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Todos.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)