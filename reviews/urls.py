from . import views
from django.urls import path


urlpatterns = [
    path('', views.BeerReviewList.as_view(), name='home')
]


