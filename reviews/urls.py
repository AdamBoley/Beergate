from . import views
from django.urls import path

urlpatterns = [
    path('', views.BeerReviewList.as_view(), name='home'),
    path('user_review/', views.UserReview.as_view(), name='user_review'),
    # path('<slug:slug>/', views.BeerReviewSingle.as_view(), name='beer_review_single'),
    path('reviews/<int:pk>/', views.BeerReviewSingle.as_view(), name='beer_review_single'),
    path('reviews/upvote/<int:pk>', views.ReviewUpvote.as_view(), name='review_upvote'),
    path('reviews/downvote/<int:pk>', views.ReviewDownvote.as_view(), name='review_downvote'),
]
