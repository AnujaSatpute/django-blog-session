from django.conf.urls import url
from .views import (UserSignUpAPIView,
                    UserLoginAPIView,
                    GetUserListView, UpdateUserAPIView)

urlpatterns = [
    url('signup', UserSignUpAPIView.as_view()),
    url('getUserList', GetUserListView.as_view()),
    url('login',UserLoginAPIView.as_view(), name="login"),
    url('updateUser/(?P<pk>.+)',UpdateUserAPIView.as_view())
]
