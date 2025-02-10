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

print(list(filter(lambda item: item["slug"] == "1234", all_posts))[0])