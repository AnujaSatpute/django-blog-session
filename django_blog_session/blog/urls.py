from django.conf.urls import url
from .views import (CreateBlogAPIView, UpdateBlogStatusAPIView, SelfBlogListView, BlogListView, GetBlogDetailsAPIView)

urlpatterns = [
    url('createBlog', CreateBlogAPIView.as_view()),
    url('updateBlog/(?P<pk>.+)', UpdateBlogStatusAPIView.as_view()),
    url('getSelfBlogList', SelfBlogListView.as_view()),
    url('getBlogList', BlogListView.as_view()),
    url('getBlogDetails/(?P<pk>.+)', GetBlogDetailsAPIView.as_view())
]
