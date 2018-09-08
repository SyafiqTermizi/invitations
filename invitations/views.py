from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import CreateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from .forms import InvitationForm
from .models import Invitation


class InvitationCreateView(LoginRequiredMixin, CreateView):
    model = Invitation
    form_class = InvitationForm

    def form_valid(self, form):
        form.instance.invited_by = self.request.user
        f = form.save()
        send_mail(
            'Subject',
            '{}'.format(f.token),
            'from@example.com',
            [f.email_address],
            fail_silently=False,
        )
        return HttpResponseRedirect(reverse('invitations:list'))


class InvitationListView(LoginRequiredMixin, ListView):
    model = Invitation


class InvitationDeleteView(LoginRequiredMixin, DeleteView):
    model = Invitation

    def get_success_url(self):
        return reverse('invitations:list')
