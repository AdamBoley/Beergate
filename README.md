# Beergate

## Code Institute Portfolio Project 4 - a Full Stack website using the Django framework and a database

Am I response image here

# Table of Contents

- [Scope](#scope)
- [Background](#background)

# Scope

The scope of this project is to create a website using the Python Django framework. The website will function as a social media site for people who like beer. 
<br>
<br>
The project will use the Django AllAuth library to allow users to create accounts and log in to the website. Once they have logged in, users will be able to post reviews of beers to help other users expand their tastes. Logged-in users will also be able to upvote and downvote these reviews, and post comments, which can also be upvoted and downvoted. 
<br>
<br>
Later, if time allows and my skills permit it, a pseudo-e-commerce function will be implemented, that will allow users to order a collection of beers using a form. EmailJS will be used to send confirmations of these orders. These orders will be fake - no payment or delivery information will be taken, and no actual beers will be sent. 
<br>
<br>

# Background

This project is inspired by the Code Institute Whiskey Drop walkthrough project that was used to demonstrate the power and responsiveness of Bootstrap. Since I am more of a beer drinker than a whiskey drinker, I made my own variation I call Beergate. [This is the repository](https://github.com/AdamBoley/bootstrap-experimentation), and [this is the deployed site on Github Pages](https://adamboley.github.io/bootstrap-experimentation/)
<br>
<br>
As a beer drinker, I enjoy exploring different beers, rather than sticking to the same brewers. The UK has a large community of small breweries who collectively produce a huge number of different beers. Given the large variety of different hops, malts and brewing techniques these breweries use, beers can differ greatly in colour and taste. 
<br>
<br>
One of the best ways to sample this variety is to visit a beer festival, such as the Reading Beer Festival or the Great British Beer Festival. At a beer festival, the custom is to drink only third-pints or half-pints, so as to sample as many beers as possible before one is rendered insensate.
<br>
<br>
However, beer festivals are not for everyone - they can be loud and crowded, and may be inaccessible for some. Also, given that the Covid-19 pandemic is still not truly over, many people, especially older or immuno-compromised people, may not feel safe attending a beer festival. This presents a dilemma - how can you sample a variety of beers without going to a beer festival?
<br>
<br>
This is where this project comes in - he aim is to replicate the purpose of a beer festival, and allow users to sample beers that they may not other be able to find. 

# Audience / Users

This project is aimed at the large community of beer drinkers in the UK who want to read reviews of different beers so that they can find more beers that they may want to try. 

# User Stories

# Features

# Function

# Development Choices

The beer review part of the project will be contained within one Django app called reviews, much like the Django Blog walkthrough project's blog app. This will include the Beer and Comment models. 

Should time permit, a second app dealing with the pseudo-e-commerce part of the project will be started. This will use a database model to contain a pre-made selection of beer, which would equate to a shipment of a case of beer. 

When formatting the admin panel, I decided to allow filtering by 5 categories - approved, created_on, brewery, type and author. Filtering by approved allows a superuser to see reviews that have not yet been approved. Filtering by created_on allows superusers to see what reviews have been posted in the last periods of time. Filtering by brewery and type allows superusers to see reviews of beers brewed by certain breweries and of beers of a certain type. Filtering by author allows superusers to see posts by certain users, which may allow them to find users who are particularly prolific. 


# Design Choices

I intend to use the background image used in the first Beergate project, that of a tall glass of beer with a dark background, which is then given some opacity to darken it off. This will apply to all pages for a uniform user experience. 
<br>
<br>
Given the dark background, each beer review post shall be held in a Bootstrap card with a light colour - white, off-white or light grey. 

# Database Models

As a Full Stack project that uses Django, this project uses models to create the database tables. These are below, and include the column headers, examples of what might be in that column and other relevant notes.

## Beer

The Beer model is used to create a table that holds all of the data to make a beer review post. 

| Column Header      | Example             | Other notes                                                      |
| -------------------|---------------------|------------------------------------------------------------------|
| name               | Golden Champion     | Unique(?), CharField, primary key?                               |
| brewery            | Hogsback            | CharField, One to Many since one brewery can make multiple beers |
| type               | Lager / Stout / Ale | CharField                                                        |
| colour             | Amber / Pale / Dark | CharField                                                        |
| alcohol_content    | 4 / 5.5             | DecimalField(max_digits=3, decimal_places=1)                     |
| image              | an image            | Cloudinary image                                                 |
| slug               | golden-champion     | SlugField, generated from name to create unique URLs             |
| content            | This beer is a beer | TextField, forms main content of post                            |
| keywords           | Hoppy / Malty       | CharField                                                        |
| hops               | American / Indian   | CharField, the hops used in the beer                             |
| upvotes            | 112                 | ManyToManyField, since many users can upvote many posts          |
| downvotes          | 21                  | ManyToManyField, since many users can downvote many posts        |
| author             | John Smith          | ForeignKey, from User table, on delete cascade                   |
| created_on         | 32nd of January     | DateTimeField                                                    |
| approved           | boolean yes/no      | BooleanField, I approve as admin superuser                       |
| aroma              | 8                   | IntegerField, with validation to accept values between 1 and 10  |
| appearance         | 5                   | IntegerField, with validation to accept values between 1 and 10  |
| taste              | 10                  | IntegerField, with validation to accept values between 1 and 10  |
| aftertaste         | 4                   | IntegerField, with validation to accept values between 1 and 10  |

The Beer model will have a Meta class that orders reviews by created_on in descending order, so that the newest reviews are displayed first

The Beer model will also have a magic string method to return the name of the beer, and two methods that deal with the numbers of upvotes and downvotes, one for each. These methods will return a count of these numbers so that they can be displayed. 

### Discussion

The Beer model contains a keyword field, which may hold any number of values. The intention is to list these as one of the first items on a beer review post, so as to give a quick summary of the beers' characteristics to a reader. 
<br>
<br>
The model also contains separate upvotes and downvotes fields, and methods to return counts of these. I am personally an avid user of Reddit, but I dislike Reddit's choice to combine upvotes and downvotes into a single number, as a user cannot see the total number of upvotes and downvotes. With separate upvote and downvote counts, the intention is to display both numbers, so that users can see how many people agree with a review, and how many people disagree, so as to be as well-informed as possible.
<br>
<br>
The Author field will contain on_delete=models.CASCADE, so that if a user's account is deleted, all beer reviews made by that user will be deleted as well. This is some defensive programming on my part, as malicious users may make posts before their accounts can be deleted using the Django administration backend. This saves an administrator having to manually delete all of that user's posts. 
<br>
<br>
The aroma, appearance, taste, aftertaste and trueness_to_style columns were added after I found [RateBeer](https://www.ratebeer.com/), and noted that said site allows numerical scores. I felt that using numerical scores along with class methods to do something with these would elevate the project. I am a member of CAMRA, and so I was able to find the criteria used by their judges in the Champion Beer of Britain competition. Explanations of these criteria are in the table below:<br>
| Criteria          | Explanation                                                                                      |
| ------------------| -------------------------------------------------------------------------------------------------|
| Aroma             | The smell of the beer - does it smell good or bad                                                |
| Appearance        | Colour, clarity, head and visual carbonation                                                     |
| Taste             | How does it taste - is it overly bitter, too weak or just right?                                 |
| Aftertaste        | How the taste lingers in the mouth                                                               |
| Trueness to Style | How it deviates from traditional beer styles - If a stout, does it taste and look like an stout? | 

After some thought, the Trueness to Style criterion was not included, as I felt that this was more of an academic ranking that could penalise beers that are different and are specifically brewed to move outside of traditional conventions, such as lighter stouts or darker pale ales. 
<br>
The slug field is used to generate unique URLs. Similar to how slugs are generated in the Django Blog walkthrough, the slugs in this project are generated primarily using the beer_review field. However, the slugs are also generated using the author field. The idea behind this is to allow multiple reviews of the same beer. Just using the beer_name would invalidate this approach, since the slugs would not be unique due to the formatting of the slug field. Combining the beer_name and author fields allows multiple reviews of the same beer, provided that each review is authored by a different user. I feel that it is reasonable that the same author would not post two reviews of the same beer. 
<br>
All other fields should be self-explanatory.

## Comment

The Comment model is used to create a table that holds all of the information to display a comment on a beer review post. 

| Column Header      | Example             | Other notes                                                      |
| -------------------|---------------------|------------------------------------------------------------------|
| post               | Guinness            | ForeignKey(Beer), on delete cascade                              |
| author             | Bob Smith           | ForeignKey(User), on delete cascade                              |
| body               | I agree with this   | TextField                                                        |
| created_on         | 33rd of February    | DateTimeField                                                    |
| upvotes            | 54                  | ManyToManyField, since many users can upvote many comments       |
| downvotes          | 67                  | ManyToManyField, since many users can downvote many comments     |

The Comment model will have a Meta class that orders comments by created_on in ascending order, so that the oldest comments are displayed first. 

The Comment model will also have a magic string method to return the comment itself followed by the name of the commenter. The Comment model will also have two other methods that deal with the numbers of upvotes and downvotes, one for each. These methods will return a count of these numbers so that they can be displayed.

### Discussion

The post and author fields will both be Foreign Keys, and will have on_delete=models.CASCADE. This means that the comment will be removed if the parent review is deleted, or if the author's account is deleted. As above, this is intended as a defensive measure, so comments made by malicious users are deleted if that malicious user's account is deleted. 
<br>
<br>
The Meta class that orders comments by created_on date so that the oldest comments are displated first is intended to simulate a conversation, so that other users can follow any discussion in the comments of a post. 


## Selection

The Selection model is used to create a table that holds 6 individual beers. 

| Column Header      | Example             | Other notes                                                      |
| -------------------|---------------------|------------------------------------------------------------------|
| name               | Pale Ales           | CharField, unique                                                |
| beer_1             | Golden Champion     | CharField                                                        |
| beer_2             | IPA                 | CharField                                                        |
| beer_3             | EPA                 | CharField                                                        |
| beer_4             | Ghost Ship          | CharField                                                        |
| beer_5             | APA                 | CharField                                                        |
| beer_6             | Kentish Pale Ale    | CharField                                                        |

### Discussion

The Selection model will be used to automatically fill out an order form when a user selects one of several pre-made selections, so that the user knows exactly what beers they wil receive. The Selection model could also be used to populate a confirmation email. 

# Deployment

This project was deployed to Heroku early on, as per the Django Blog walkthrough project. 

## Project set up

Given that this is a Django project, a number of terminal commands must be run before any real development work can begin:

Install Django v3 and the Gunicorn web-server: <br>
`pip3 install 'django<3' gunicorn`

Install libraries necessary for working with PostgresQL:<br>
`pip3 install dj_database_url psycopg2`

Install libraries needed for Cloudinary:<br>
`pip3 install dj3_cloudinary_storage`

Create a requirements.txt file:<br>
`pip3 freeze --local > requirements.txt`

Create a new Django Project:<br>
`django-admin startproject beergate .`

Create a new Django app for the beer reviews: <br>
`python3 manage.py startapp reviews`

Then add 'reviews' to beergate/settings.py

Now migrate the changes made by starting the beergate project and the reviews app to the database:<br>
`python3 manage.py migrate`

Check that Django and all other libraries have been installed by running the project locally:<br>
`python3 manage.py runserver`

Create a new Heroku app and add on the heroku-postgres module. Copy the DATABASE_URL config var

Create an env.py file. At the top, import os and create an os environment variable called DATABASE_URL and assign it the value from Heroku as a string
Then add a second os environment variable called SECRET_KEY and assign it a random value
Add this to the Heroku config vars

Add a conditional import to settings.py to import env.py
Update the DATBASES variable in settings.py to use the heroku DATABASE_URL config var

Then migrate the changes again:
`python3 manage.py migrate`

Add Port 8000 to Heroku config vars

### Cloudinary

Create a Cloudinary account, copy API environment variable

Add CLOUDINARY_URL environment variable to env.py and paste in
Add same to Heroku config vars

Add DISABLE_COLLECTSTATIC to Heroku config vars as well, with a value of 1

Add static file storage and media file storage to settings.py
Add local host and heroku app name to ALLOWED_HOSTS
Add the TEMPLATES_DIR to settings.py

Create media, static and templates directories at top-level of the repository

Create a Procfile

### Models

Create Models in reviews/models.py

Prepare migrations:
`python3 manage.py makemigrations`

Load models into database and create tables:
`python3 manage.py migrate`

### Superuser and Django admin panel set up

Create a superuser:
`python3 manage.py createsuperuser`

Run a development server to access the Django admin panel:
`python3 manage.py runserver`

Append `/admin/` to the URL

Login to Django admin backend using superuser credentials

(solve problem relating to automatic upgrade to Django v4.1 - see bugs section)

Update admin.py to allow superusers to create beer reviws in the Django admin panel

Install Summernote to allow rich text in admin panel:
`pip3 install django-summernote`

Add summernote to requirements.txt:
`pip3 freeze --local > requirements.txt`

Add summernote to INSTALLED_APPS in settings.py

Update urls.py, then admin.py

Migrate again:
`python3 manage.py migrate`

### Views

Views and URLs created as per walkthrough videos. Beer review posts not displaying. 

Problem may lie in views.py, where reviews are filtered by approved=True. May need to update model to use the Draft / Published IntegerField system of the Django Blog. 

Views created successfully and above problem solved - see bugs section. 

### Single beer review page



## Development process

Now that Django has been set up:

I need to change up the process that is used in the Walkthrough

Users should be able to make posts

This will require appropriation of the code for leaving a comment

I foresee two methods by which a user could make a post:
- Hide the form where a user makes a post behind a button on the index page. When the user clicks this button, the form is revealed and the user may write their post
- Provide a button with an anchor link that takes the user to a separate page where the post is written - USE THIS APPROACH
    - This is a separation of concerns matter - the index page is displaying posts, the single_review page is for viewing a post and the make_a_post page is for writing a post.



For beer_review_single:
<!-- <a href="{% url 'beer_review_single' beer_review.slug %}" class="post-link">
                                    This calls the second path in urlpatterns in blog/urls.py
                                    <h2 class="card-title">{{ beer_review.beer_name }}</h2>
                                </a> -->


To do:

- Review generic placeholder image - it is too small
- Rework Bootstrap card structure
- provide a consistent aspect ratio for post images
- Background image not displaying on deployed site




# Bugs

When trying to deploy an initial blank version of the project to Heroku, I ran into an error, with Heroku being unable to build a wheel for backports.zoneinfo

Some Googling revealed that the problem could be to do with the version of Python that Heroku uses, and that a possible fix could be to add a runtime.txt file to the repository to specify the exact version of Python that should be used. Said file was added with `python-3.8.13`.

In the end, I noted that this was extraneous, since INSTALLED_APPS was missing a comma. Once added, Heroku was able to build and deploy the app properly


After creating a superuser to access the Django backend, I ran into a 403 error when trying to login using that superuser via the admin login page. 

Some Googling found [this StackOverflow page](https://stackoverflow.com/questions/70285834/forbidden-403-csrf-verification-failed-request-aborted-reason-given-for-fail/70326426#70326426). Though this should apply only to Django v4.x.x , where I specifically installed Django v3, as per the walkthrough videos. 

Running the command `python3 -m django --version`, obtained from [this StackOverflow page](https://stackoverflow.com/questions/6468397/how-to-check-django-version), to check the version of Django installed, I found that the project was using Django v4. The Django documentation says that Django v4.1 was released on 3/8/22, about 4 days before I tried to access the backend. I can only conclude that Django upgraded from v3 to v4.1 automatically. 

To solve the error, I found [this StackOverflow page](https://stackoverflow.com/questions/29573163/django-admin-login-suddenly-demanding-csrf-token), which provided a line of code that must be added to settings.py:

CSRF_TRUSTED_ORIGINS = ['https://*.YOUR_DOMAIN.COM'], replacing YOUR_DOMAIN.COM with the URL of the Gitpod workspace I was using, prefixed with `8000-` to account for the development server. 

This worked, and allowed me to login to the Django backend without issue. The code above appears to override the need to provide a CSRF token when performing actions from this workspace. This may present a vulnerability, as a CSRF token is Django's way of protecting sites against malicious users, and the code in settings.py overrides that. I asked my Mentor, and his response was....



When attempting to render an BeerReview database entry, I initially could not get a Bootstrap card holding the various fields to display. I thought that this may have been a problem with my views. Where the Django Blog uses a status field to mark a post as either draft or published, I am merely using an approved field, and then filtering posts to display by the boolean value in the approved field. Removing this stipulation did not work. 

I then viewed the index.html page in the Dev Tools and found that the card was not even rendering, and that the code was stopping at the Templating Language For Loop. I had been using for `beer_review in beer_review_list`. I then consulted the [Django documentation on class-based views](https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/), and found that their example code uses `for publisher in object_list`. I followed their pattern and changed `beer_review_list` to `object_list`. This worked, and the index page displayed the test beer review that I had made in the database. 





# Testing

## Manual testing

Can I create an account
<br>
Can I sign-in to that account?
<br>
Can I make a post?
<br>
Can I make a comment?
<br>

## Automated testing

PyTest

# Technologies

Slack
<br>
LucidChart
<br>
Django
<br>
AllAuth
<br>
Github
<br>
Gitpod
<br>
Heroku
<br>
Cloudinary

# Credits
