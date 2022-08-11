from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import BeerReview
from .forms import CommentForm, BeerReviewForm


# Create your views here.

class BeerReviewList(generic.ListView):
    model = BeerReview
    queryset = BeerReview.objects.filter(approved=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4


class BeerReviewSingle(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = BeerReview.objects.filter(approved=True)
        beer_review = get_object_or_404(queryset, slug=slug)
        comments = beer_review.comments.filter(approved=True).order_by('created_on')
        upvoted = False
        downvoted = False
        if beer_review.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        if beer_review.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True

        return render(
            request,
            "beer_review_single.html",
            {
                "beer_review": beer_review,
                "comments": comments,
                "commented": False,
                "upvoted": upvoted,
                "downvoted": downvoted,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = BeerReview.objects.filter(approved=True)
        beer_review = get_object_or_404(queryset, slug=slug)
        comments = beer_review.comments.filter(approved=True).order_by('created_on')
        upvoted = False
        downvoted = False
        if beer_review.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        if beer_review.downvotes.filter(id=self.request.user.id).exists():
            downvoted = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.beer_review = beer_review
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "beer_review_single.html",
            {
                "beer_review": beer_review,
                "comments": comments,
                "commented": True,
                "upvoted": upvoted,
                "downvoted": downvoted,
                "comment_form": CommentForm()
            }
        )

