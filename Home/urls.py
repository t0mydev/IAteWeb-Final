from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('Home/', views.IAteHome, name='IAteHome'),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('survey/<int:id>/',views.show_survey,name="show_survey"),
    path('function3/',views.Horariopref,name="Horariopref"),
    path('function2/',views.estadocasinoview,name="estadocasino"),
    path('function1/',views.estadofila,name="estadofila")
]
