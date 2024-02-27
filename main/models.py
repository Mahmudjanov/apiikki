from django.db import models


class BookCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/books/')
    rate = models.IntegerField()


class Author(models.Model):
    name = models.CharField(max_length=255)
    book = models.ManyToManyField(Book, blank=True)
    image = models.ImageField(upload_to='img/author/')


class BookDetail(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    page = models.IntegerField(null=True, blank=True)
    year = models.DateField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    time = models.FloatField(null=True, blank=True)
    storage = models.FloatField(null=True, blank=True)
    like_tahririyat = models.BooleanField(default=False, null=True, blank=True)
