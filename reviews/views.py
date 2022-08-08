from django.shortcuts import render
from django.views import generic
from .models import BeerReview


# Create your views here.

class BeerReviewList(generic.ListView):
    model = BeerReview
    queryset = BeerReview.objects.filter(approved=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8

