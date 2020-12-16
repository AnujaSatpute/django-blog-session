from rest_framework import status
from rest_framework.generics import (GenericAPIView,
                                     CreateAPIView,
                                     ListAPIView, UpdateAPIView)
from rest_framework.response import Response
from .serializers import (BlogSerializer, UpdateBlogStatusSerializer, )
from .models import Blog
from users.models import User


class CreateBlogAPIView(CreateAPIView):
    serializer_class = BlogSerializer

    def post(self, request, *args, **kwargs):

        print("REQUEST DATA" , request.data)
        serializer =self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data)




class BlogListView(ListAPIView):
    serializer_class = BlogSerializer

    def post(self, request, *args, **kwargs):
        data = list()
        get_status = request.data["status"]
        blog_data = Blog.objects.filter(status=get_status)
        serializer = self.get_serializer(blog_data, many=True)

        for blog in serializer.data:
            get_user = User.objects.filter(id=blog["user_id"]).values("first_name", "last_name", "email", "description",
                                                                      "linkedin_url", "contact_number")

            print("USER_DETAILS", get_user)

            data.append({
                "id": blog["id"],
                "title": blog["title"],
                "content": blog["content"],
                "status": blog["status"],
                "user_id": blog["user_id"],
                "first_name": get_user[0]["first_name"],
                "last_name": get_user[0]["last_name"],
                "email": get_user[0]["email"],
                "description": get_user[0]["description"],
                "linkedin_url": get_user[0]["linkedin_url"],
                "contact_number": get_user[0]["contact_number"],
                "created_at": blog["created_at"],
                "updated_at": blog["updated_at"]
            })
        return Response(data, status.HTTP_200_OK)




class SelfBlogListView(ListAPIView):
    serializer_class = BlogSerializer

    def post(self, request, *args, **kwargs):
        data = list()
        user_id = request.data["user_id"]
        blog_data = Blog.objects.filter(status="DRAFT").filter(user_id=user_id)
        serializer = self.get_serializer(blog_data, many=True)

        for blog in serializer.data:

            get_user = User.objects.filter(id=blog["user_id"]).values("first_name", "last_name", "email", "description",
                                                                      "linkedin_url", "contact_number")

            data.append({
                "id": blog["id"],
                "title": blog["title"],
                "content": blog["content"],
                "status": blog["status"],
                "user_id": blog["user_id"],
                "first_name": get_user[0]["first_name"],
                "last_name": get_user[0]["last_name"],
                "email": get_user[0]["email"],
                "description": get_user[0]["description"],
                "linkedin_url": get_user[0]["linkedin_url"],
                "contact_number": get_user[0]["contact_number"],
                "created_at": blog["created_at"],
                "updated_at": blog["updated_at"]
            })
        return Response(data, status.HTTP_200_OK)




class UpdateBlogStatusAPIView(UpdateAPIView):
    serializer_class = UpdateBlogStatusSerializer


    def get_queryset(self):
        blog_id =self.kwargs['pk']
        return Blog.objects.filter(id=blog_id)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = request.data["status"]

        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid(raise_exception=True):
             self.partial_update(serializer)

        return Response(serializer.data, status.HTTP_200_OK)

class GetBlogDetailsAPIView(ListAPIView):
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        data = list()
        blog_id = self.kwargs["pk"]
        blog_data = Blog.objects.filter(id=blog_id)
        serializer = self.get_serializer(blog_data, many=True)
        for blog in serializer.data:
            get_user = User.objects.filter(id=blog["user_id"]).values("first_name", "last_name", "email", "description",
                                                                      "linkedin_url", "contact_number")
            data.append({
                "id": blog["id"],
                "title": blog["title"],
                "content": blog["content"],
                "status": blog["status"],
                "user_id": blog["user_id"],
                "first_name": get_user[0]["first_name"],
                "last_name": get_user[0]["last_name"],
                "email": get_user[0]["email"],
                "description": get_user[0]["description"],
                "linkedin_url": get_user[0]["linkedin_url"],
                "contact_number": get_user[0]["contact_number"],
                "created_at": blog["created_at"],
                "updated_at": blog["updated_at"]
            })
        return Response(data, status.HTTP_200_OK)