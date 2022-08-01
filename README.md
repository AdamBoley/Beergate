# Beergate

## Code Institute Portfolio Project 4 - a Full Stack website using Django and a database

Am I response image here

# Table of Contents

- [Scope](#scope)
- [Background](#background)

# Scope

The scope of this project is to create a website using the Python Django framework. The website will function as a social media site for people who like beer. 
<br>
The project will use the Django AllAuth library to allow users to create accounts and log in to the website. Once they have logged in, users will be able to post reviews of beers to help other users expand their tastes. Logged-in users will also be able to upvote and downvote these reviews, and post comments, which can also be upvoted and downvoted. 
<br>
Later, if time allows and my skills permit it, a pseudo-e-commerce function will be implemented, that will allow users to order a collection of beers using a form. EmailJS will be used to send confirmations of these orders. These orders will be fake - no payment or delivery information will be taken, and no actual beers will be sent. 
<br>

# Background

This project is inspired by the Code Institute Whiskey Drop walkthrough project that was used to demonstrate the power and responsiveness of Bootstrap. Since I am more of a beer drinker than a whiskey drinker, I made my own variation I call Beergate. [This is the repository](https://github.com/AdamBoley/bootstrap-experimentation), and [this is the deployed site on Github Pages](https://adamboley.github.io/bootstrap-experimentation/)
<br>
As a beer drinker, I enjoy exploring different beers, rather than sticking to the same brewers. The UK has a large community of small breweries who collectively produce a huge number of different beers. Given the large variety of different hops, malts and brewing techniques these breweries use, beers can differ greatly in colour and taste. 
<br>
One of the best ways to sample this variety is to visit a beer festival, such as the Reading Beer Festival or the Great British Beer Festival. At a beer festival, the custom is to drink only third-pints or half-pints, so as to sample as many beers as possible before one is rendered insensate.
<br>
However, beer festivals are not for everyone - they can be loud and crowded, and may be inaccessible for some. Also, given that the Covid-19 pandemic is still not truly over, many people, especially older or immuno-compromised people, may not feel safe attending a beer festival. This presents a dilemma - how can you sample a variety of beers without going to a beer festival?
<br>
This is where this project comes in - he aim is to replicate the purpose of a beer festival, and allow users to sample beers that they may not other be able to find. 

# Audience / Users

This project is aimed at the large community of beer drinkers in the UK who want to read reviews of different beers so that they can find more beers that they may want to try. 

# User Stories

# Features

# Function

# Development Choices

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
| alcohol Content    | 4 / 5.5             | IntegerField(?)                                                  |
| image              | an image            | Cloudinary image                                                 |
| slug               | golden-champion     | SlugField, generated from name to create unique URLs             |
| description        | This beer is a beer | TextField, forms main content of post                            |
| keyword_1          | Hoppy               | CharField, first keyword to quickly describe a beer              |
| keyword_2          | Fruity              | CharField, second keyword to quickly describe a beer             |
| keyword_3          | Malty               | CharField, third keyword to quickly describe a beer              |
| hops               | American / Indian   | CharField, the hops used in the beer                             |
| upvotes            | 112                 | ManyToManyField, since many users can upvote many posts          |
| downvotes          | 21                  | ManyToManyField, since many users can downvote many posts        |
| author             | John Smith          | ForeignKey, from User table, on delete cascade                   |
| created_on         | 32nd of January     | DateTimeField                                                    |
| excerpt            | This beer is nice   | TextField, used as a tag-line under a post name                  |

The Beer model will have a Meta class that orders reviews by created_on in descending order, so that the newest reviews are displayed first

The Beer model will also have a magic string method to return the name of the beer, and two methods that deal with the numbers of upvotes and downvotes, one for each. These methods will return a count of these numbers so that they can be displayed. 

### Discussion

The Beer model contains three keyword fields. The intention is to list these as one of the first items on a beer review post, so as to give a quick summary of the beers' characteristics to a reader. 
<br>
The model also contains separate upvotes and downvotes fields, and methods to return counts of these. I am personally an avid user of Reddit, but I dislike Reddit's choice to combine upvotes and downvotes into a single number, as a user cannot see the total number of upvotes and downvotes. With separate upvote and downvote counts, the intention is to display both numbers, so that users can see how many people agree with a review, and how many people disagree, so as to be as well-informed as possible.
<br>
The Author field will contain on_delete=models.CASCADE, so that if a user's account is deleted, all beer reviews made by that user will be deleted as well. This is some defensive programming on my part, as malicious users may make posts before their accounts can be deleted using the Django administration backend. This saves an administrator having to manually delete all of that user's posts. 
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
The Meta class that orders comments by created_on date so that the oldest comments are displated first is intended to simulate a conversation, so that other users can follow any discussion in the comments of a post. 

# Deployment

This project was deployed to Heroku early on, as per the Django Blog walkthrough project. 

# Testing

## Manual testing

Can I create an account

Can I sign-in to that account?

Can I make a post?

Can I make a comment?

## Automated testing

PyTest

# Technologies

Slack

LucidChart

Django

AllAuth

Github

Gitpod

Heroku

# Credits
