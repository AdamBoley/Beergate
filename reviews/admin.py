from django.contrib import admin
from .models import BeerReview, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(BeerReview)
class BeerReviewAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('beer_name', 'author')}
    list_filter = ('approved', 'created_on', 'brewery', 'type', 'author')
    list_display = ('beer_name', 'type', 'brewery', 'slug', 'created_on', 'approved',)
    search_fields = ['beer_name', 'brewery', 'type', 'colour', 'hops', 'alcohol_content', 'content']
    summernote_fields = ('content')
    actions = ['approve_beer_review']

    def approve_beer_review(self, request, queryset):
        queryset.update(approved=True)

# admin.site.register(BeerReview)

# future work notes:
# list display adds columns to the Django admin panel that show fields
# could add keywords, alcohol_content, etc, for more information
# search fields allows searching of the database for particular entries
# could add aroma, appearance, taste, aftertaste for additional searching functionality
# 'content', 'colour', 'alcohol_content', 'hops', 'author'
# it appears that having author in search_fields does not work


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_filter = ('approved', 'created_on', 'beer_review', 'author')
    list_display = ('beer_review', 'author', 'comment_body' , 'created_on', 'approved')
    search_fields = ['beer_review', 'author', 'approved']
    summernote_fields = ('comment_body')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)
