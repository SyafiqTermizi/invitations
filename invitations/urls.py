from django.urls import path

from . import views


app_name = "invitations"
urlpatterns = [
    path('create/', views.InvitationCreateView.as_view(), name='create'),
    path('', views.InvitationListView.as_view(), name='list'),
    path('<int:pk>/delete/', views.InvitationDeleteView.as_view(), name='delete'),
]