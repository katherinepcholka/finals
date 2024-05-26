from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from petcare import settings
from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'default_image': settings.DEFAULT_USER_IMAGE}

    def get_success_url(self):
        return reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

