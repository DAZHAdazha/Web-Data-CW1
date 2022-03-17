from django.urls import path
from .views import viewProfessors,viewModules,viewRegister,viewLogin,viewLogout,viewAverage,viewRating

urlpatterns = [
    path('viewProfessors', viewProfessors, name='viewProfessors'),
    path('viewModules', viewModules, name='viewModules'),
    path('viewRegister', viewRegister, name='viewRegister'),
    path('viewLogin', viewLogin, name='viewLogin'),
    path('viewLogout', viewLogout, name='viewLogout'),
    path('viewAverage', viewAverage, name='viewAverage'),
    path('viewRating', viewRating, name='viewRating'),
]