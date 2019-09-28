from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(pk=user.id)

    # def retrieve(self, request, pk=None):
    #     queryset = CustomUser.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     print(user)
    #     serializer = CustomUserSerializer(user)
    #     print(serializer.data)
    #     print(repr(serializer))
    #     return Response(serializer.data)


    
