from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, ApiKeyView, RestaurantsView

app_name = 'authentication'
urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('api_keys/', ApiKeyView.as_view()),
    path('restaurants/', RestaurantsView.as_view()),

]
