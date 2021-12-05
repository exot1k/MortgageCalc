from django.urls import path
from rest_framework import routers

from mainapp.views import MortgageViewSet

ApiRouter = routers.SimpleRouter()

extra_urlpatterns = [
    path('mortgage/', MortgageViewSet.as_view()),
]
urlpatterns = []
urlpatterns += ApiRouter.urls
urlpatterns.extend(extra_urlpatterns)
