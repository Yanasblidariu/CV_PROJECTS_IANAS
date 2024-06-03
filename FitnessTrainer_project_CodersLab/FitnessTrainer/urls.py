"""
URL configuration for FitnessTrainer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BodyFreakApp.views import FrontPageView
from BodyFreakApp.views import GetPrescriptionView
from BodyFreakApp.views import MemberAccount
from BodyFreakApp.views import WorkoutPlan
from BodyFreakApp.views import NutritionPlan
from BodyFreakApp.views import Feedback
from BodyFreakApp.views import ExerciseList
from BodyFreakApp.views import DietList
from BodyFreakApp.views import BaseView
from BodyFreakApp.views import ViewUsers
from BodyFreakApp.views import LoginView
from BodyFreakApp.views import LogoutView
from BodyFreakApp.views import AddUserView
from BodyFreakApp.views import ResetpasswordView
from BodyFreakApp.views import UserView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',FrontPageView.as_view(),name="front_page"),
    path('get-prescription/',GetPrescriptionView.as_view(),name="get_prescription"),
    path('user-login/',MemberAccount.as_view(),name="member_account"),
    path('workout_plan/',WorkoutPlan.as_view(),name="workout_plan"),
    path('nutrition_plan/',NutritionPlan.as_view(),name="nutrition_plan"),
    path('feedback/',Feedback.as_view(),name="feedback"),
    path("", BaseView.as_view()),
    path("list_users/", ViewUsers.as_view()),
    path("login/", LoginView.as_view(), name="login_view"),
    path("logout/", LogoutView.as_view(), name="logout_view"),
    path("add_user/", AddUserView.as_view(), name="add_user"),
    path("reset_password/<int:id>/", ResetpasswordView.as_view(), name="reset_password"),
    path("user/<int:id>/", UserView.as_view(), name="user"),
    path('exercises/', ExerciseList.as_view(), name='exercises_list'),
    path('diets/', DietList.as_view(), name='diet_list'),
    ]
    
    