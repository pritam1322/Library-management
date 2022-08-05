from django.contrib import admin
from django.urls import path
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views



urlpatterns = [
    path('', views.home, name='library-home'),
    path('library_admin/', views.library_admin, name='library-library_admin'),
    path('customerregister', views.customerregister, name='library-customerregister'),
    path('customerlogin', views.customerlogin, name='library-customerlogin'),
    path('issued_book', views.issued_book, name='library-issued_book'),
    path('admin_page', views.admin_page, name='library-admin_page'),
    path('view_customers', views.view_customers, name='library-view_customers'),
    path('view_books', views.view_books, name='library-view_books'),
    path('returned_book', views.returned_book, name='library-returned_book'),
    path('add_book_details', views.add_book_details, name='library-add_book_details'),
    path('view_returned_books', views.view_returned_books, name='library-view_returned_books'),
    path('view_issued_books', views.view_issued_books, name='library-view_issued_books'),
    path('view_transac2',views.view_transac2, name='library-view_transac2' ),
    path('delete_customer/<int:myid>/',views.delete_customer, name='library-delete_customer' ),
    path('logout',views.Logout, name='logout' )
]

#urlpatterns += staticfiles_urlpatterns()