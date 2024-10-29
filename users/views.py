from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from .models import User

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User

    def get_object(self):
        return self.request.user
