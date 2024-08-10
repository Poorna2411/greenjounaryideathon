from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import register_team, complete_transaction, registration_success


urlpatterns = [
    path('', views.home, name='home'),
    path('rules/', views.rules, name='rules'),
    path('about/', views.about, name='about'),
    path('register/', register_team, name='register'),
    path('transaction/', complete_transaction, name='complete_transaction'),
    path('success/', registration_success, name='registration_success'),
    path('contact/', views.contact, name='contact'),
    path('contact_complete/', views.contact_complete, name='contact_complete'),
    path('login/', views.login_view, name='login'),
    path('submission/', views.submission, name='submission'),
    path('upload_c/', views.upload_c, name='upload_c'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('bot/', views.chatbot_page, name='chatbot_page'),
    path('response/', views.chatbot_response, name='chatbot_response'),
]
