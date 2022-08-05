from tkinter.tix import Select
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import CustomerDetails,Book,BooksDetails, ReturnedBook, customer_login,Transaction2
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
      return render(request, 'library/home.html')



def customerregister(request):
      
      if request.method == 'POST':
            username = request.POST['username']
            password=request.POST['password']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email_id=request.POST['email_id']
            mobile_number=request.POST['mobile_number']
            address=request.POST['address']
            

            cus = CustomerDetails(c_id=username, full_name=first_name, last_name=last_name, email_id=email_id,   mobile_number=mobile_number, address=address)

            cus.save()
            alert = True
            return render(request, "library/customerregister.html", {'alert':alert})


      return render(request, 'library/customerregister.html')

def customerlogin(request):
      
      if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = CustomerDetails.objects.filter(username=username, password=password).exists()

            if user is not None:
                  login(request, user)
                  if request.user.is_superuser:
                        return HttpResponse("You are not registered!!")
                  else:
                        return redirect("/library-home")
            else:
                  alert = True
                  return render(request, "library/customerregister.html", {'alert':alert})
      
      return render(request, 'library/customerlogin.html')

def library_admin(request):
      if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                  login(request, user)
                  if request.user.is_superuser:
                        return render(request, "library/admin_page.html")
                  else:
                        return HttpResponse("You are not an admin.")
            else:
                  alert = True
                  return render(request, 'library/library_admin.html', {'alert':alert})
      return render(request, 'library/library_admin.html')



            
@login_required(login_url = '/library-library_admin')
def issued_book(request):
      if request.method == 'POST':
            b_id = request.POST['b_id']
            c_id = request.POST['c_id']
            issued_date = request.POST['issued_date']
            date_of_return = request.POST['date_of_return']
            due_date = request.POST['due_date']
            ISBN = request.POST['ISBN']
            book_name = request.POST['book_name']
            
            name = CustomerDetails.objects.values_list('full_name')
            name_c_id = CustomerDetails.objects.values_list('c_id')
            for i in range(len(name)):
                  if name[i][:1] == "A" and c_id == name_c_id[i]:
                        t2 = Transaction2(first_name=name, book_name=book_name)
                        t2.save()
                        return render(request, 'library/issued_book.html')
            
            books = Book.objects.create(b_id=b_id, c_id=c_id, issued_date=issued_date, date_of_return=date_of_return, due_date=due_date, ISBN=ISBN, book_name=book_name)
            books.save()
            alert = True
            
            return render(request, 'library/issued_book.html', {'alert':alert})
      return render(request, 'library/issued_book.html')

@login_required(login_url = '/library-library_admin')
def returned_book(request):
      if request.method == 'POST':
            b_id = request.POST['b_id']
            issued_date = request.POST['issued_date']
            c_id = request.POST['c_id']
            ISBN = request.POST['ISBN']
            return_date = request.POST['return_date']
            book_name = request.POST['book_name']
            
            b = ReturnedBook.create(b_id=b_id, issued_date=issued_date, c_id=c_id, ISBN=ISBN, return_date=return_date, book_name=book_name)
            b.save()
            alert = True
            
            return render(request, 'library/returned_book.html')
      
      return render(request, 'library/returned_book.html')

#@login_required(login_url = '/library-library_admin')
def add_book_details(request):
      if request.method == 'POST':
            b_id = request.POST['b_id']
            edition = request.POST['edition']
            ISBN = request.POST['ISBN']
            volume = request.POST['volume']
            author = request.POST['author']
            availability = request.POST['availabilitye']
            book_name = request.POST['book_name']
            price = request.POST['price']

            bd = BooksDetails.objects.create(b_id=b_id, edition=edition, ISBN=ISBN, volume=volume, author=author, availability=availability, book_name=book_name, price=price)
            bd.save()
            
            return render(request, 'lbrary/add_book_details.html')
      
      return render(request, 'lbrary/add_book_details.html')
            
@login_required(login_url = '/library-library_admin')
def admin_page(request):
      return render(request, 'library/admin_page.html')

@login_required(login_url = '/library-library_admin')
def view_customers(request):
      cus = CustomerDetails.objects.all()
      return render(request, 'library/view_customers.html',{'customers': cus})

@login_required(login_url = '/library-library_admin')
def view_books(request):
      boo = BooksDetails.objects.all()
      return render(request, 'library/view_books.html', {'books':boo})

@login_required(login_url = '/library-library_admin')
def view_returned_books(request):
      ret = ReturnedBook.objects.all()
      return render(request, 'library/view_returned_books.html', {'returned_books':ret}) 

@login_required(login_url = '/library-library_admin')
def view_issued_books(request):
      iss = Book.objects.all()
      return render(request, 'library/view_issued_books.html',{'issued':iss})

@login_required(login_url = '/library-library_admin')
def view_transac2(request):
      tr = Transaction2.objects.all()
      return render(request, 'library/view_transac2.html', {'transaction':tr})

def delete_customer(request,myid):
      tr3 = CustomerDetails.objects.filter(id = myid)
      tr3.delete()
      return redirect("/librarylibrary_admin")

def Logout(request):
      logout(request)
      return redirect ("/library")