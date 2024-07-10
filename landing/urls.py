from django.urls import path

from landing.views import MyView

app_name = 'landing'

urlpatterns = [
    path('landing/', MyView.as_view(), name='landing'),
]
