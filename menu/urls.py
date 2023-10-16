from django.urls import path
from .views import menuView

urlpatterns = [
    path('<str:name>', menuView, name='getEl'),
    path('', menuView, name='default'),
]
