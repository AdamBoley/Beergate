from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class BeerReview(models.Model):
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
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="beer_review")
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']
        verbose_name = "beer review"

    def __str__(self):
        return f"A review of {self.beer_name} by {self.author}"

    def description(self):
        return f"A {self.colour} {self.type} by {self.brewery}"
    
    def short_description(self):
        return f"Described as {self.keywords}"

    def review_upvotes(self):
        return self.upvotes.count()

    def review_downvotes(self):
        return self.downvotes.count()


class Comment(models.Model):
    beer_review = models.ForeignKey(BeerReview, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    upvotes = models.ManyToManyField(User, related_name='comment_upvotes', blank=True)
    downvotes = models.ManyToManyField(User, related_name='comment_downvotes', blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name = "review comment"
    
    def __str__(self):
        return f"{self.author} said: {self.comment}"
    
    def comment_upvotes(self):
        return self.upvotes.count()

    def comment_downvotes(self):
        return self.downvotes.count()

