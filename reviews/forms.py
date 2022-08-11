from .models import Comment, BeerReview
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_body',)






class BeerReviewForm(forms.ModelForm):
    class Meta:
        model = BeerReview
        fields = (
            'beer_name',
            'brewery',
            'type',
            'colour',
            'alcohol_content',
            'hops',
            'image',
            'keywords',
            'content',
            'aroma',
            'appearance',
            'taste',
            'aftertaste'
        )