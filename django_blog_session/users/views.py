from rest_framework import status
from rest_framework.generics import (CreateAPIView,
                                     DestroyAPIView,
                                     ListAPIView,
                                     GenericAPIView,
                                     UpdateAPIView)
from rest_framework.response import Response
from .serializers import (UserSignUpSerializer,
                          UserLoginSerializer,
                          UpdateUserSerializer )
from .models import User


class UserSignUpAPIView(CreateAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA", request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            obj = User.objects.get(email=request.data["email"])

            response_data = {
                "id": obj.id,
                "first_name": obj.first_name,
                "last_name": obj.last_name,
                "email": obj.email,
                "username": obj.username
            }
            return Response(response_data)
        else:
            return Response(serializer.errors)


class GetUserListView(ListAPIView):
    serializer_class = UserSignUpSerializer

    def get_queryset(self):
        return User.objects.filter(is_superuser=False)

    def get(self, request, *args, **kwargs):
        serializer = super().list(request, *args, **kwargs)
        print("SERIALIZER", serializer.data)
        return Response(serializer.data)


class UserLoginAPIView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA", request.data)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            obj = serializer.user

            response_data = {
                "id": obj.id,
                "first_name": obj.first_name,
                "last_name": obj.last_name,
                "email": obj.email,
                "username": obj.username
            }
            return Response(response_data)
        else:
            return Response(serializer.errors)




class UpdateUserAPIView(UpdateAPIView):
    serializer_class = UpdateUserSerializer


    def get_queryset(self):
        users_id =self.kwargs['pk']
        return User.objects.filter(id=users_id)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = request.data["status"],
        instance.email = request.data["email"],
        instance.first_name = request.data["first_name"],
        instance.last_name = request.data["last_name"],
        instance.description = request.data["description"],
        instance.linkedin_url = request.data["linkedin_url"],
        instance.contact_number= request.data["contact_number"]


        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid(raise_exception=True):
             self.partial_update(serializer)

        return Response(serializer.data, status.HTTP_200_OK)



class DeleteUserView(DestroyAPIView) :
    def delete(self, request, *args, **kwargs):
        user_id =self.kwargs['pk']
        User.objects.filter(id=user_id).delete()
        return  Response(status.HTTP_204_NO_CONTENT)
