from django.shortcuts import render

# Create your views here.

all_posts = [
    {
        "slug": "1234",
        "title": "Learn Django",
        "author": "Erfan Rajati",
        "image": "mountain.jpg",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam consectetur quaerat, distinctio id facilis facere"
    },
    {
        "slug": "4311",
        "title": "Learn Python",
        "author": "Erfan Rajati",
        "image": "mountain.jpg",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam consectetur quaerat, distinctio id facilis facere"
    },
    {
        "slug": "1423",
        "title": "Learn Flask",
        "author": "Erfan Rajati",
        "image": "mountain.jpg",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam consectetur quaerat, distinctio id facilis facere"
    },
]


def posts(request):
    return render(request, "posts/index.html", context={"data":all_posts})


def post_details(request, slug):
    post = list(filter(lambda item: item["slug"] == slug, all_posts))[0]
    print(post)
    return render(request, "post_details/post_details.html", context=post)