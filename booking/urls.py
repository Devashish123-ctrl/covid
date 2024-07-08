from django.urls import path
from .views import signup_view, login_view, centers_view, slots_view,user_logout

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('centers/', centers_view, name='centers'),
    path('slots/', slots_view, name='slots'),
    path('logout/',user_logout)
]
