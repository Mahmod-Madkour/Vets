### account/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [

    # Login & Register
    path('', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),

    # Prifile
    path('profile/', views.user_profile, name='user_profile'),
    path('profile_everyone/<pk_user>/', views.user_profile_everyone, name='user_profile_everyone'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('update_password/', views.update_password, name='update_password'),

    # Prifile -> Posts
    path('profile/posts', views.profile_posts, name='profile_posts'),
    # Prifile -> Questions
    path('profile/questions', views.profile_questions, name='profile_questions'),
    # Prifile -> Diseases
    path('profile/profile_diseases', views.profile_diseases, name='profile_diseases'),


    # Reset Password
    path('password_reset/', PasswordResetView.as_view(template_name='auth/password_reset.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='auth/password_reset_complete.html'), name='password_reset_complete'),

    ####################################################################################################
    
    # Create a New Post
    path("new_post/", views.create_post, name="create_post"),

    # All Posts
    path('posts/', views.post_home, name='post_home'),
    
    # Like Post
    path("posts/<pk_post>/", views.like_post, name="like_post"),

    # All Comment
    path("post_detail/<pk_post>/", views.post_detail, name="post_detail"),
    # Like Comment
    path("post_detail/<pk_post>/<pk_comment>/", views.like_comment, name="like_comment"),

    # All Replaies
    path("comment_detail/<pk_post>/<pk_comment>/", views.comment_detail, name="comment_detail"),
    # Like Replay
    path("comment_detail/<pk_post>/<pk_comment>/<pk_replay>/", views.like_replay, name="like_replay"),

    # Update Post
    path("update_post/<pk_post>/", views.update_post, name="update_post"),
    # Delete Post
    path("delete_post/<pk_post>/", views.delete_post, name="delete_post"),

    # Update Comment
    path("update_comment/<pk_post>/<pk_comment>/", views.update_comment, name="update_comment"),
    # Delete Comment
    path("delete_comment/<pk_post>/<pk_comment>/", views.delete_comment, name="delete_comment"),

    # Update Replay
    path("update_replay/<pk_post>/<pk_comment>/<pk_replay>/", views.update_replay, name="update_replay"),
    # Delete Replay
    path("delete_replay/<pk_post>/<pk_comment>/<pk_replay>/", views.delete_replay, name="delete_replay"),

    ####################################################################################################

    # All Questions
    path("questions/", views.question_home, name="question_home"),

    # All Questions Same Status
    path("status/<status>/", views.status_question, name="status_question"),

    # Ask Question
    path("ask/", views.ask_question, name="ask_question"),

    # Detail Of One Question & All Answers & 
    path("detail_question/<int:pk_question>/", views.detail_question, name="detail_question"),

    # Update Question
    path("update/<int:pk_question>/", views.update_question, name="update_question"),

    # Delate Question
    path("delete_question/<int:pk_question>/", views.delete_question, name="delete_question"),

    # Delate Answer
    path("delete_answer/<int:pk_question>/<int:pk_answer>/", views.delete_answer, name="delete_answer"),

    # Vote Answer
    path("vote_answer/<pk_question>/<pk_answer>/", views.vote_answer, name="vote_answer"),
    
    ####################################################################################################

    # All Diseases
    path("diseases/", views.disease_home, name="disease_home"),

    # All Questions Same Status
    path("category/<category>/", views.category_disease, name="category_disease"),
    
    # Add Disease
    path("add/", views.add_disease, name="add_disease"),

    # Detail Of One Disease & All Therapy
    path("detail_disease/<int:pk_disease>/", views.detail_disease, name="detail_disease"),

    # Delate Disease
    path("delete_disease/<int:pk_disease>/", views.delete_disease, name="delete_disease"),

    # Delate Therapy
    path("delete_therapy/<int:pk_disease>/<int:pk_therapy>/", views.delete_therapy, name="delete_therapy"),

    # Delate Therapy Replay
    path("delete_therapy_replay/<pk_disease>/<pk_therapy>/<pk_replay>/", views.delete_therapy_replay, name="delete_therapy_replay"),

    # Detail Of One Therapy & All Replaies
    path("detail_therapy/<int:pk_disease>/<int:pk_therapy>/", views.detail_therapy, name="detail_therapy"),

]

