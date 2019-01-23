
from django.conf.urls import url, include
from django.contrib import admin
from socialPosts import views

urlpatterns = [
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)$', views.PostDetail.as_view()),
    url(r'^comments/$', views.CommentList.as_view()),
    url(r'^comment/(?P<pk>[0-9]+)$', views.CommentDetail.as_view()),
    url(r'^tags/$', views.TagList.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)$', views.TagDetail.as_view()),
    url(r'^user/$', views.UserPosts.as_view()),
    url(r'^feed/$', views.FeedList.as_view()),
    url(r'^update/$', views.PostUpdate.as_view()),
]