from . import views
from django.urls import path


urlpatterns = [
    path('', views.BeerReviewList.as_view(), name='home'),
    path('<slug:slug>/', views.BeerReviewSingle.as_view(), name='beer_review_single')
]


