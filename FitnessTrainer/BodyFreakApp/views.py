from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .my_forms import LoginForm, AddUserForm, ResetPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import re

# Create your views here.

class FrontPageView(View):
    def get(self,request):
        return render(request,"front_page.html")
    
class GetPrescriptionView(View):
    def get(self,request):
        return render(request,"get_prescription.html")

class MemberAccount(View):
    def get(self, request):
        return render(request, "member_acount.html")
    
class WorkoutPlan(View):
    def get(self,request):
        return render(request,"workout_plan.html")
    
class ExerciseList(View):
    def get(self,request):
        return render(request,"exercises_list.html")
    
class DietList(View):
    def get(self,request):
        return render(request,"diet_list.html")
    
class NutritionPlan(View):
    def get(self,request):
        return render(request,"nutrition_plan.html")
    
class Feedback(View):
    def get(self,request):
        return render(request,"feedback.html")


class ViewUsers(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, "users_view.html", {"users": users})
    

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login_view.html", {"form": form})


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                # return HttpResponse("User is logged in!")
                return redirect("user", id=user.id)
            else:
                return HttpResponse("Authentication error!")
            
        return HttpResponse("YOU ARE NOT REGISTERED!")
    

class LogoutView(View):
    def get(self, request):
            logout(request)
            return redirect("login_view")
    


class BaseView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "index.html", {"username": request.user.username})
        else:
            return render(request, "index.html", {"username": "None"})

    
class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, "add_user.html", {"form": form })
    
    def post(self, request):
        form = AddUserForm(request.POST)
       
        if form.is_valid():
            username = form.cleaned_data["username"]
            password_1 = form.cleaned_data["password_1"]
            password_2 = form.cleaned_data["password_2"]
            name = form.cleaned_data["name"]
            surname = form.cleaned_data["surname"]
            email = form.cleaned_data["email"]
            if len(User.objects.filter(username=username)) > 0:
                return HttpResponse("User already exists!")
            if password_1 != password_2:
                return HttpResponse("Passwords do not match!")
            
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

            if not re.fullmatch(regex, email):
                return HttpResponse("Email is not valid!")

            User.objects.create_user(username=username, password=password_1, first_name=name, last_name=surname, email=email)
            # am adaugat o variabila de sesiune pentru a pute aface redirect si a afisa informatia ca user-ul a fost creat
            request.session["message"] = "User was created!"
            return redirect("login")


        return HttpResponse("Form is not valid!")


class ResetpasswordView(LoginRequiredMixin, PermissionRequiredMixin,  View):
    # petnru a verifica permisiunile pt un user: usr.has_perm("app1.change_user")


    # TODO: verify redirect
    login_url = '/login/'
    # redirect_field_name = 'redirect_to'
    permission_required = "app1.change_user"
    
    def get(self, request, id):
        form = ResetPasswordForm()
        curret_user = User.objects.get(id=id)
        return render(request, "reset_password.html", {"user": curret_user, "form": form })
    
    def post(self, request, id):

        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            pass_1 = form.cleaned_data["password_1"]
            pass_2 = form.cleaned_data["password_2"]
            if pass_1 != pass_2:
                return HttpResponse("Passwords do not match!")
            current_user = User.objects.get(id=id)
            current_user.set_password(pass_1)
            current_user.save()
            request.session["message"] = "Password was successfully changed!"
            return redirect("login_view") 

        return HttpResponse("Form is not valid!")
    


class UserView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, id):
        # fac astfel incat, user-ul care face request la pagina curenta sa fie exact cel logat. Altfel, reimtiem user-ul la pagina de logare.
        if request.user.id == id:
            current_user = User.objects.get(id=id)
            return render(request, "user.html", {"user": current_user})
        else:
            request.session["message"] = "Currently logged user has no access to this page!"
            return redirect("login_view")

