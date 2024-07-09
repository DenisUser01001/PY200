from django.urls import path
from .views import template_view, index_view, login_view, register_view, \
    logout_view, user_detail_view, get_text_json, MyFormView, MyLoginView
from .views import TemplView, MyTemplView

from django.contrib.auth.views import LoginView

app_name = 'app'

urlpatterns = [
    path('', index_view, name='index'),
    path('template/', MyFormView.as_view(), name='template'),  # тестирую разное отображение № 4
    path('template/', MyTemplView.as_view(), name='template'),  # тестирую разное отображение № 3
    path('template/', TemplView.as_view(), name='template'),    # тестирую разное отображение № 2
    path('template/', template_view, name='template'),    # тестирую разное отображение № 1
    path('login/', LoginView.as_view(template_name='app/login.html',
                                     redirect_authenticated_user=True), name='login'),  # тестирую разное отображение № 6
    path('login/', MyLoginView.as_view(), name='login'),  # тестирую разное отображение № 5
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('profile/', user_detail_view, name='user_profile'),
    path('get/text/', get_text_json),
]
