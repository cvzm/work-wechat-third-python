from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('callback/instruct', views.callback_instruct),

    path('service/get_suite_token', views.get_suite_token),
]