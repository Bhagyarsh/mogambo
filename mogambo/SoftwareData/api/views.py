from rest_framework import generics ,permissions
from SoftwareData.models import Software,Tag,Category
from .serializers import (SoftwareSerializers, CategorySerializers,
                SoftwareListSerializers,SoftwareRUDSerializers)
from django.db.models import Q
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from .pagination import  SoftwareListOffsetPagination#b
class SoftwareRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = SoftwareSerializers

    def get_queryset(self):
        return Software.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Command.objects.get(pk=pk)


class SoftwarelistAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = []
    serializer_class = SoftwareListSerializers
    pagination_class = SoftwareListOffsetPagination
    def get_queryset(self, *arg, **kwargs):
        request = self.request
        query = request.GET.get("q")
        print(query)
        if query is not None:

            lookup = (Q(name__icontains=query) |
                      Q(description__icontains=query) |
                      Q(Tag__name__icontains=query))
            #      Q(platform__platform__icontains=query))
            return Software.objects.filter(lookup)

        return Software.objects.all()

class SoftwareRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareRUDSerializers
    lookup_field = 'slug'
    def get_queryset(self, *arg, **kwargs):
        Software.objects.all()

class SoftwarecreateAPIView(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = []
    queryset = Tag.objects.all()
    serializer_class = SoftwareRUDSerializers

    def perform_create(self, serializer):
         serializer.save(user=self.request.user)
# class CategoryRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializers
#     lookup_field = 'slug'
#     def get_queryset(self, *arg, **kwargs):
#         Category.objects.all()

# class CategoryRUDCreateView(generics.CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializers
#     lookup_field = 'slug'
#     def get_queryset(self, *arg, **kwargs):
#         Category.objects.all()
