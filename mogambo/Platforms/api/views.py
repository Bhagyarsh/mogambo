from rest_framework import generics
from Platforms.models import Command
from .serializers import CommandSerializers

class CommandRetrieveView(generics.RetrieveAPIView):

    lookup_field = 'pk'
    serializer_class = CommandSerializers
    def get_queryset(self):
        return Command.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Command.objects.get(pk=pk)
