from django.urls import path
from .views import kayu


urlpatterns = {
    path('', kayu, name='kayu'),
}
