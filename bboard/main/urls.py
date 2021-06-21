from django.urls import path
from .views import index, other_page, BBLoginView, profile

app_name = 'main'
urlpatterns = [
    path('account/profile',profile, name='profile'),
    path('account/login', BBLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]

