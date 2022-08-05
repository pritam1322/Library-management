from django.contrib import admin
from .models import Book, BooksDetails,ReturnedBook,CustomerDetails,customer_login
# Register your models here.
admin.site.register(BooksDetails)
admin.site.register(Book)
admin.site.register(CustomerDetails)
admin.site.register(ReturnedBook)
admin.site.register(customer_login)