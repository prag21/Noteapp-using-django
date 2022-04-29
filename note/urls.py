from .views import logout, sign,base,login,logout,note,edit
from django.urls import path

urlpatterns=[
    path('',base,name='base'),
    path('sign',sign.as_view(),name='sign'),
    path('login',login.as_view(),name='login'),
    path('logout',logout,name='logout'),
    path('note',note.as_view(),name='note'),
    path('edit',edit.as_view(),name='edit'),
    ]