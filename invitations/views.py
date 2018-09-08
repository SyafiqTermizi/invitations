from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import InvitationForm
from .models import Invitation


class InvitationCreateView(LoginRequiredMixin, CreateView):
    model = Invitation
    form_class = InvitationForm

    def form_valid(self, form):
        form.instance.invited_by = self.request.user
        return HttpResponseRedirect(reverse('invitations:list'))


class InvitationListView(LoginRequiredMixin, ListView):
    model = Invitation


class InvitationDeleteView(LoginRequiredMixin, DeleteView):
    model = Invitation
