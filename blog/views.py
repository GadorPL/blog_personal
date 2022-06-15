from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Michał",
        "date": date(2022, 6, 15),
        "title": "Mountain Hiking",
        "excerpt": "There's noting like the views you get when hiking in the mountains! "
                  "And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
            Pol, a bene itineris tramitem, coordinatae! Make it so, alignment!
            Our shining harmony for heaven is to capture others extraordinarily.
            You have to listen, and feel trust by your luring.
            Jolly! Pieces o' pestilence are forever proud.   
            
            Pol, a bene itineris tramitem, coordinatae! Make it so, alignment!
            Our shining harmony for heaven is to capture others extraordinarily.
            You have to listen, and feel trust by your luring.
            Jolly! Pieces o' pestilence are forever proud.
            
            Pol, a bene itineris tramitem, coordinatae! Make it so, alignment!
            Our shining harmony for heaven is to capture others extraordinarily.
            You have to listen, and feel trust by your luring.
            Jolly! Pieces o' pestilence are forever proud.
        """,
    },

    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Michał",
        "date": date(2022, 6, 14),
        "title": "Programming is Fun",
        "excerpt": "There's noting like the views you get when hiking in the mountains! "
                   "And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
            Pol, a bene itineris tramitem, coordinatae! Make it so, alignment!
            Our shining harmony for heaven is to capture others extraordinarily.
            You have to listen, and feel trust by your luring.
            Jolly! Pieces o' pestilence are forever proud.   

            Pol, a bene itineris tramitem, coordinatae! Make it so, alignment!
            Our shining harmony for heaven is to capture others extraordinarily.
            You have to listen, and feel trust by your luring.
            Jolly! Pieces o' pestilence are forever proud.

            Pol, a bene itineris tramitem, coordinatae! Make it so, alignment!
            Our shining harmony for heaven is to capture others extraordinarily.
            You have to listen, and feel trust by your luring.
            Jolly! Pieces o' pestilence are forever proud.
        """,
    },

    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Michał",
        "date": date(2022, 6, 13),
        "title": "Nature At Its Best",
        "excerpt": "There's noting like the views you get when hiking in the mountains! "
                   "And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
            Pol, a bene itineris tramitem, coordinatae! Make it so, alignment!
            Our shining harmony for heaven is to capture others extraordinarily.
            You have to listen, and feel trust by your luring.
            Jolly! Pieces o' pestilence are forever proud.   

            Pol, a bene itineris tramitem, coordinatae! Make it so, alignment!
            Our shining harmony for heaven is to capture others extraordinarily.
            You have to listen, and feel trust by your luring.
            Jolly! Pieces o' pestilence are forever proud.

            Pol, a bene itineris tramitem, coordinatae! Make it so, alignment!
            Our shining harmony for heaven is to capture others extraordinarily.
            You have to listen, and feel trust by your luring.
            Jolly! Pieces o' pestilence are forever proud.
        """,
    }
]


def get_date(post):
    return post['date']


# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")


