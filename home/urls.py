from django.urls import path
from home import views

app_name='home'

urlpatterns =[
    path('',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('insert/',views.insert,name='insert'),
    path('blogposts/',views.blogposts,name='blogposts'),
    path('blogpst/<int:id>',views.blogpst,name='blogpst'),
]