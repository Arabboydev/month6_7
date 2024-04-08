from django.db import models
from student.models import Student

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.first_name} {self.last_name}"

class Comments(models.Model):
    text = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Kitobning Nomi")
    description = models.TextField(verbose_name="Izoh")
    price = models.FloatField()
    comments = models.ManyToManyField(Comments)
    count = models.IntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_created=True)
    # autocomplete_fields = ['author__first_name']

    def __str__(self):
        return f"{self.title} {self.price}"

class BookingBook(models.Model):
    student = models.ManyToManyField(Student)
    book = models.ManyToManyField(Book)
    take_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} {self.book}"