from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# last two are for validation - see Django documentation on valudation

# Create your models here.


def validate_within_limits(value):
    """
    Method for validation of aroma, appearance, taste and aftertaste
    integer fields in BeerReview model
    """
    if value < 1:
        raise ValidationError(
            _('%(value)s is less than 1'),
            params={'value': value},
        )
    elif value > 10:
        raise ValidationError(
            _('%(value)s is greater than 10'),
            params={'value': value},
        )


class BeerReview(models.Model):
    """
    The model for a beer review post, much like a blog post
    Contains all database fields that I want to be injected into a page
    """
    beer_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    brewery = models.CharField(max_length=200)
    type = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    alcohol_content = models.DecimalField(max_digits=3, decimal_places=1)
    hops = models.CharField(max_length=100)
    image = CloudinaryField('image', default='placeholder')
    keywords = models.CharField(max_length=200)
    content = models.TextField()
    upvotes = models.ManyToManyField(User, related_name='review_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='review_downvotes', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="beer_review")
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    aroma = models.IntegerField(validators=[validate_within_limits])
    appearance = models.IntegerField(validators=[validate_within_limits])
    taste = models.IntegerField(validators=[validate_within_limits])
    aftertaste = models.IntegerField(validators=[validate_within_limits])

    class Meta:
        """
        Meta class for the BeerReview class
        Supplies a verbose name and
        indicates that reviews should be ordered so that newest display first
        """
        ordering = ['-created_on']
        verbose_name = "beer review"

    def __str__(self):
        """
        Magic string method to return the beer that is being
        reviewed and the name of the review
        """
        return f"A review of {self.beer_name} by {self.author}"

    def description(self):
        """
        A string method similar to the above
        Returns a short description of the review
        """
        return f"A {self.colour} {self.type} by {self.brewery}"

    def short_description(self):
        """
        A string method that returns the keywords used to describe the beer
        """
        return f"Described as {self.keywords}"

    def review_upvotes(self):
        """
        Returns a count of the number of upvotes
        These may then be displayed
        """
        return self.upvotes.count()

    def review_downvotes(self):
        """
        Returns a count of the number of downvotes
        These may then be displayed
        """
        return self.downvotes.count()

    def aggregate_score(self):
        """
        Averages the 4 IntegerField scores
        Gives an overall impression of the beer
        """
        aroma = self.aroma
        appearance = self.appearance
        taste = self.taste
        aftertaste = self.aftertaste
        aggregate = (aroma + appearance + taste + aftertaste) / 4
        return aggregate


class Comment(models.Model):
    """
    A model for comments that can be made on beer review posts
    """
    beer_review = models.ForeignKey(BeerReview, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='comment_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='comment_downvotes', blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Meta class for the comment class
        Supplies a verbose name and
        indicates that comments should be displayed with the oldest first
        This mimics a conversation
        """
        ordering = ['created_on']
        verbose_name = "review comment"

    def __str__(self):
        """
        A magic string method for the comment class
        """
        return f"{self.author} said: {self.comment_body}"

    def comment_upvotes(self):
        """
        Returns a count of the number of upvotes
        These may then be displayed
        """
        return self.upvotes.count()

    def comment_downvotes(self):
        """
        Returns a count of the number of downvotes
        These may then be displayed
        """
        return self.downvotes.count()


