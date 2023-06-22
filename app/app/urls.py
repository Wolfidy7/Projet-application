from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path

import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('home/', blog.views.home, name='home'),
    path('p_submit/',blog.views.submitSubject, name='p_submit'),
    path('e_submit/',blog.views.submitWork, name='e_submit'),
    path('p_redirect/',blog.views.p_redirect, name='p_redirect'),
    path('e_redirect/',blog.views.e_redirect, name='e_redirect'),
    path('mes_notes/',blog.views.view_notes, name='notes'),
    path('statistics/',blog.views.view_statistics, name='stats'),
    path('available_subjects/', blog.views.show_availables, name='availables'),
    path('mes_notes1/', blog.views.view_student_notes, name='notes'),
]
