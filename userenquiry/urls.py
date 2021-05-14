from django.urls import path, re_path

from userenquiry import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("userform/", views.userform, name="userform"),
    path("finaldata/", views.finaldata, name="finaldata"),
    re_path(r'^updatestatus/(?P<id>\d+)$', views.updatestatus, name='updatestatus'),

]
