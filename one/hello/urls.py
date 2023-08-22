from django.urls import path, include
from hello.views import home_page

urlpatterns = [
    path('', home_page, name="home_page"),
]
    