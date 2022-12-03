from django.contrib.auth.models import User
from django.db import models



class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts', null=True)
    author = models.ManyToManyField(User, through='Like', related_name='books')

    def __str__(self):
        return f"{self.time_create}"


class Comment(models.Model):
    owner = models.ForeignKey('Women', related_name='comments', on_delete=models.CASCADE)
    time_now = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=True)
    author_1 = models.ManyToManyField(User, through='Otvet', related_name='load')

    def __str__(self):
        return f"{self.time_now}"


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE, null=True)

    # posts = models.ManyToManyField('Women', related_name='categories', blank=True)

    def __str__(self):
        return f"{self.name}"


class Like(models.Model):
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Good'),
        (3, 'Fine'),
        (4, 'Amazing'),
        (5, 'Incredible'),
    )
    book = models.ForeignKey('Women', on_delete=models.CASCADE, related_name='blok')
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boks', null=True)
    rate = models.PositiveIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'{self.book}'


class Otvet(models.Model):
    subjects = models.ForeignKey('Comment', related_name='ragu', on_delete=models.CASCADE)
    time_now = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    author_1 = models.ForeignKey(User, related_name='ragu', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.author_1}"


