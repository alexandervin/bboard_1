from django.urls import path
from .views import index, other_page, BBLoginView, profile, BBLogoutView, ChangeUserInfoView, BBPasswordChangeView

app_name = 'main'
urlpatterns = [
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_chenge'),
    path('accounts/profile/', profile, name='profile'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]

