from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategory,CategoryView,CategoryListView,LikeView,AddCommentView\
# from . import views
from django.urls import path, include

urlpatterns = [
    # path('', views.home, name='home')
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('add_category/',AddCategory.as_view(),name='add_category'),
    path('update_post/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('delete_post/<int:pk>/remove',DeletePostView.as_view(),name='delete_post'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('category_list/',CategoryListView,name='category_list'),
    path('like/<int:pk>',LikeView,name='like_post'),
    
]
