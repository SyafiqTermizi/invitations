from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView

from .forms import InvitationForm
from .models import Invitation


class InvitationCreateView(CreateView):
    model = Invitation
    form_class = InvitationForm


class InvitationListView(ListView):
    model = Invitation


class InvitationDeleteView(DeleteView):
    model = Invitation
