from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db import IntegrityError


# Create your views here.
def home(request):
  if not request.user.is_authenticated: 
        return redirect('login_user')
  
  return render(request, "home.html")




# def register(request):
#   if request.user.is_authenticated:  
#         return redirect('home')
  
#   if request.method == 'POST':
#     first_name= request.POST['first_name']
#     last_name= request.POST['last_name']
#     username= request.POST['username']
#     email= request.POST['email']
#     password= request.POST['password']
#     confirm_password= request.POST['confirm_password']

#     if password == confirm_password :
#       if User.objects.filter(username= username).exists():
#         messages.info(request, 'username already exists')
#         return redirect('register')
#       else:
#         user= User.objects.create_user(username= username, password= password, email= email, first_name= first_name, last_name= last_name)
#         user.set_password(password)
#         user.is_staff= True
#         user.save()
#         print('success')
#         return redirect('login_user')

#   else:
#     print('This is not post method')
#     return render(request, 'register.html')
  




# def login_user(request):
#   if request.user.is_authenticated:  
#         return redirect('home')
  
#   if request.method == 'POST':
#     username= request.POST['username']
#     password= request.POST['password']

#     if not username or not password:
#             messages.error(request, "All fields are required.")
#             return render(request, 'login.html')

#     user= auth.authenticate(username= username, password= password)

#     if user is not None:
#       auth.login(request, user)
#       return redirect('home')
#     else:
#       messages.info(request, 'Invalid username or password')
    
#   else:
#     return render(request, 'login.html')
  



def register(request):
    if request.user.is_authenticated:  
        return redirect('home')
  
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            try:
                # Check if the username already exists
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exists')
                    return redirect('register')

                # Create the user
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.is_staff = True
                user.save()

                print('Registration successful')
                return redirect('login_user')

            except IntegrityError:
                messages.error(request, 'An error occurred during registration. Please try again.')
                return redirect('register')

            except Exception as e:
                messages.error(request, f"An unexpected error occurred: {str(e)}")
                return redirect('register')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        print('This is not a POST method')
        return render(request, 'register.html')






def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Authenticate the user
            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                # Log the user in
                auth.login(request, user)
                return redirect('home')  # Redirect to a success page
            else:
                # If authentication fails
                messages.error(request, 'Invalid username or password')
                return redirect('login_user')

        except Exception as e:
            # Handle any unexpected errors
            messages.error(request, f'An error occurred: {str(e)}')
            return redirect('login')

    return render(request, 'login.html')



def logout_user(request):
  auth.logout(request)
  return redirect('login_user')
  # return redirect('home')




