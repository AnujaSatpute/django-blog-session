from django.conf.urls import  url
from .views import  (CreateBlogAPIView,)

urlpatterns =[
    url('createBlog',CreateBlogAPIView.as_view() )
]