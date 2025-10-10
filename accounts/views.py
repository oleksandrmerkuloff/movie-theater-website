from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

from accounts.models import User


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        return context


class ChangeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'accounts/change.html'
    fields = ['fname', 'lname', 'email', 'sex', 'birthday', 'client_type']
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def test_func(self):
        """Allow only the owner of the profile to change it."""
        obj = self.get_object()
        return self.request.user == obj or self.request.user.is_admin

    def get_success_url(self):
        return reverse_lazy('user-profile', kwargs={'pk': self.object.pk})


class DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('home')  # change this to your actual homepage url

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def test_func(self):
        """Allow only the user themselves or admin to delete."""
        obj = self.get_object()
        return self.request.user == obj or self.request.user.is_admin
