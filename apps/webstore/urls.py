from django.urls import path
from .views import *


urlpatterns = [
    path('', kayu, name='kayu'),
    path('shop/', shop, name='shop'),
    path('blog/', blog, name='blog'),
    path('soporte/', soporte, name='soporte'),
    path('faq/', faq, name='faq'),
]
