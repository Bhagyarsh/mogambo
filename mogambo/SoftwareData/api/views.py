from rest_framework import generics
from SoftwareData.models import Software
from .serializers import SoftwareSerializers, SoftwareListSerializers
from django.db.models import Q


class SoftwareRetrieveView(generics.RetrieveAPIView):
    lookup_field = 'slug'
    serializer_class = SoftwareSerializers

    def get_queryset(self):
        return Software.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Command.objects.get(pk=pk)


class SoftwarelistAPIView(generics.ListAPIView):
    queryset = Software.objects.all()
    serializer_class = SoftwareListSerializers

    def get_queryset(self, *arg, **kwargs):
        request = self.request
        query = request.GET.get("q")
        if query is not None:

            lookup = (Q(name__icontains=query) |
                      Q(description__icontains=query) |
                      Q(Tag__name__icontains=query))
            #      Q(platform__platform__icontains=query))
            return Software.objects.filter(lookup)

        return Software.objects.none()
