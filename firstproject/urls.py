"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.contrib.auth import views as auth_views
from myapp.forms import EmailValidationOnForgotPassword
from django.contrib.auth.forms import PasswordResetForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/',views.userprofileview,name='profile'),
    # path('path/',views.page,name='path'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.logout_view,name='logout'),
    path('deleteprofile/',views.delete_profile,name='deleteprofile'),
    path('list/',views.profilelist,name='list'),
    path('update/',views.update_profile,name='update'),
    path('change_password/',views.change_password,name='update'),
    path('getprofile/',views.get_profile,name='getprofile'),
    path('createpost/',views.create_post,name='createpost'),
    path('deletepost/',views.delete_post,name='deletepost'),
    path('deleteonepost/<int:id>/',views.delete_one_post,name='deleteonepost'),
    path('comment/',views.MyComment.as_view(),name='comment'),
    path('createcomment/',views.createtcomment,name='comment'),
    # path('updatecomment/',views.updatecomment,name='comment'),
    path('deletecomment/',views.deletecomment,name='deletecomment'),
    path('like_comment/',views.like_comment,name='like_comment'),
    path('reset/',views.password_reset_request),





    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',form_class=PasswordResetForm),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset'),

]

if settings.DEBUG:urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
