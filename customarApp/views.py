from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login

from .forms import CustomarRegistrationForm
from django.views.generic import View
# # Create your views here.
#
# # =================== Author
# class LoginView(View):
#     template_name = 'auth/login.html'
#     def get(self, request):
#         return render(request, self.template_name)
#
#     def post(self, request):
#         if request.method == "POST":
#             user = request.POST.get('login_user')
#             password = request.POST.get('login_password')
#             auth = authenticate(request, username=user, password=password)
#             if auth is not None:
#                 login(request, auth)
#                 return redirect('mainApp:index')
#             else:
#                 print("login error")
#         return render(request, self.template_name)
#
# # ======================================= Customar Registration


class CustomarRegistration(View):
    template_name = 'customarapp/registration.html'
    def get(self, request):
        form = CustomarRegistrationForm(request.POST or None, request.FILES or None)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    def post(self, request):
        form = CustomarRegistrationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
        return render(request, self.template_name, {"form": form})