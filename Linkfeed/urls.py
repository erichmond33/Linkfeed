from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('profile', views.current_user_profile, name='current_user_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    # path('profile/<int:user_id>/', views.profile, name='profile_with_id'),
    path("profile", views.profile, name="profile"),
    path("feed", views.feed, name="feed"),
    path("post/<int:post_id>/", views.post, name="post"),
    path("post/<int:post_id>/add_comment/", views.add_comment, name="add_comment"),
    path("Linkfeed/post/<int:post_id>/delete_post/", views.delete_post, name='delete_post'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path("post/<int:post_id>/edit/", views.edit_post, name="edit_post"),  # URL for editing a post
    path("create_post/", views.create_post, name="create_post"),
    path('post/<int:pk>/like', views.like_view, name='like_post'),  # URL for liking/unliking a post
    path('followers/<str:username>/', views.followers_view, name='followers'),
    path('following/<str:username>/', views.following_view, name='following'),
    path('follow/<str:username>/', views.follow_view, name='follow_profile'),
  

]
         
         

