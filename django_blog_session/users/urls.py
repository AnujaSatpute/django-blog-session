from django.conf.urls import url
from .views import UserSignUpAPIView, GetUserListView

urlpatterns = [
    url('signup', UserSignUpAPIView.as_view()),
    url('getUserList', GetUserListView.as_view())
]
