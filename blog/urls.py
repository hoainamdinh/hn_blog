from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blogger/<int:pk>', views.BlogByUserView.as_view(), name='blog_by_user'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog_detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blog/<int:pk>/comment/', views.CommentCreate.as_view(), name='blog_comment'),
]
