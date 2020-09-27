from rest_framework.generics import ( GenericAPIView,
                                      CreateAPIView,
                                      ListAPIView)
from rest_framework.response import Response
from .serializers import (BlogSerializer,)
from .models import Blog


class CreateBlogAPIView(CreateAPIView):
    serializer_class = BlogSerializer

    def post(self, request, *args, **kwargs):

        print("REQUEST DATA" , request.data)
        serializer =self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)