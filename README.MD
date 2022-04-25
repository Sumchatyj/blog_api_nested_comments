# Blog api with nested comments

## How to start

Clone repository to your working directory.
Activate your venv.
Install requirements:

`$ pip install -r requirements.txt`

Do all migrations, be sure that you are in directory with manage.py:

`$ python manage.py migrate`

Then just run the server:

`$ python manage.py runserver`

API documentation available at:

<http://127.0.0.1:8000/swagger/>

For correct operation of swagger statics on nonlocal hosts execute this command:

`$ python manage.py collectstatic`

## What you can do

Create posts, add comments including nested comments.

- Check comments to the post till third level on this endpoint: <http://127.0.0.1:8000/post-comments/{post_id}>
- Check all nested comments on this endpoint: <http://127.0.0.1:8000/comments/{comment_id}>
