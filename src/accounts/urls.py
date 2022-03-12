from django.urls import path

from .views import AccountLoginView
from .views import AccountLogoutView
from .views import AccountRegistrationDoneView
from .views import AccountRegistrationView
from .views import AccountUpdateProfileView
from .views import account_profile_view
from .views import user_activate

app_name = 'accounts'

urlpatterns = [
    path('registration/асtivate/<str:sign>/', user_activate, name='register_activate'),
    path('registration/done/', AccountRegistrationDoneView.as_view(), name='registration_done'),
    path('registration/', AccountRegistrationView.as_view(), name='registration'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('profile/', account_profile_view, name='profile'),
    path('profile_change/', AccountUpdateProfileView.as_view(), name='profile_change'),
]
