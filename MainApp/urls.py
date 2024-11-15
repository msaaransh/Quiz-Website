from django.urls import path
from MainApp import views

urlpatterns = [
	path("", views.home, name="home"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
	path("profile/", views.profile, name="profile"),
    path("quiz/", views.Quiz, name="quiz"),
	path("result/", views.result, name="result"),
    path("all_quiz/", views.all_quiz, name="all_quiz"),
	path("submit/", views.submit, name="submit"),
	path("login/", views.login, name="login"),
    path("sign_up/", views.sign_up, name="sign_up"),
	path("forgot/", views.forgot, name="forgot"),




]
