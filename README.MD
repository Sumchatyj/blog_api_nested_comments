# Blog api with nested comments

## Description
Commentary api-service for blog or social network. Supports nested comments.
You can create posts, add comments including nested comments.

- Check comments to the post till third level on this endpoint: <http://127.0.0.1:8000/post-comments/{post_id}>
- Check all nested comments on this endpoint: <http://127.0.0.1:8000/comments/{comment_id}>

## Getting started

### Dependencies

* python 3.7
* django 4.0.4
* djangorestframework 3.13.1
* django_mptt 0.13.4

### Installing

Clone repository to your working directory.
Activate your venv:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
```

Do all migrations, be sure that you are in directory with manage.py:

```
python manage.py migrate
```
Collect static

```
python manage.py collectstatic
```

### Executing program

Run the server:

```
python manage.py runserver
```

API documentation available at:

<http://127.0.0.1:8000/swagger/>
