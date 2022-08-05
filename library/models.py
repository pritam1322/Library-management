from statistics import mode
from django.db import models
from matplotlib.style import available

# Create your models here.

class customer_login(models.Model):
      name = models.CharField(max_length=64)
      password = models.CharField(max_length=64)

class BooksDetails(models.Model):
      b_id = models.CharField(max_length=64)
      edition = models.CharField(max_length=64)
      ISBN = models.PositiveIntegerField()
      volume = models.IntegerField()
      author = models.CharField(max_length=64)
      available = models.CharField(max_length=4)
      book_name = models.CharField(max_length=64)
      price = models.IntegerField()
      
class Transaction2(models.Model):
      first_name = models.CharField(max_length=64)
      book_name = models.CharField(max_length=64)

class ReturnedBook(models.Model):
      b_id = models.IntegerField()
      issued_date = models.DateField()
      c_id = models.CharField(max_length=64)
      ISBN = models.PositiveIntegerField()
      return_date = models.DateField()
      book_name = models.CharField(max_length=64)

class CustomerDetails(models.Model):
      c_id = models.CharField(max_length=64)
      full_name = models.CharField(max_length=64)
      last_name = models.CharField(max_length=64)
      email_id = models.CharField(max_length=64)
      mobile_number = models.IntegerField()
      address = models.CharField(max_length=64)
      
      
class Book(models.Model):
      b_id = models.CharField(max_length=64)
      c_id = models.CharField(max_length=64)
      issued_date = models.DateField()
      date_of_return = models.DateField()
      due_date = models.DateField()
      ISBN = models.PositiveIntegerField()
      book_name = models.CharField(max_length=64)
      
      def __str__(self,):
            return str(self.name) + " ["+str(self.isbn)+']'
      
      