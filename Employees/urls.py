from django.urls import path
from . import views

urlpatterns = [
        path("", views.preview, name="preview"),
        path("home/<str:usrCode>", views.home, name="home"),
        path("login", views.login_usr, name="login_usr"),
        path("logout", views.logout_usr, name="logout_usr"),
        path("signup", views.signup_usr, name="signup_usr"),
        path("addEmp/<str:usrCode>",views.addEmp, name="addEmp"),
        path("search/<str:usrCode>", views.search, name="search"),
        path("knowMore/<str:usrCode>/<str:staffId>", views.knowMore, name="knowMore"),
        path("myaccount/<str:usrCode>", views.myAcc, name="myAcc"),
        path("editEmp/<str:usrCode>/<str:staffId>", views.editEmp, name="editEmp"),
        path("changePwd", views.changePwd, name="changePwd"),
        path("team", views.team, name="team"),
]
