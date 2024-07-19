# Import necessary modules and functions
from django.shortcuts import render, redirect,reverse
from django.contrib.auth import authenticate, login, logout
from .models import DietPlan, WorkoutPlan,Membership,CustomUser,Shipment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse
# View function for the index page
def index(request):
    # Render the index.html template
    return render(request, 'index.html')

# View function for the signup page
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Your signup logic
        if password == password2: 
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request,'Email Already Used')
                return redirect('signup')
            elif CustomUser.objects.filter(username=username).exists():
                messages.error(request,'Username Already Used')
                return redirect('signup')
            else:
                user = CustomUser.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

# View function for the login page
def login_view(request):

    # Check if the request method is POST
    if request.method == 'POST':
        # Get the username and password from the request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        # Check if the user is authenticated
        if user is not None:
            # Login the user
            login(request, user)
            # Check if the user is an admin or staff member
            if user.is_superuser:
                # Redirect to the Django admin interface or staff dashboard page
                return redirect('/admin/')
            elif user.is_staff:
                return redirect('/admin/')
            elif Membership.objects.filter(trainee=user).exists():  # Check if user has a membership
                # Redirect to the trainee dashboard if not an admin or staff
                return redirect('/trainee_dashboard/')
            else:
                return redirect('index')
        else:
            # Handle invalid login credentials
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    
    # Render the login.html template for GET requests
    return render(request, 'login.html')

# View function for logging out
def logout_view(request):
    # Logout the user
    logout(request)
    # Redirect to the index page
    return redirect('index')

# View function for the trainee dashboard

@login_required
def trainee_dashboard(request):
    # Retrieve the current user
    user = request.user
    
    # Retrieve the diet plan and workout plan for the user
    diet_plan = DietPlan.objects.filter(trainee=user).first()
    workout_plan = WorkoutPlan.objects.filter(trainee=user).first()
    membership = Membership.objects.filter(trainee=user).first()

    # Prepare context data to be passed to the template
    context = {
        'username': user.username,
        'diet_plan': diet_plan,
        'workout_plan': workout_plan,
        'membership': membership, 
        'user_image':user.image
        
    }

    # Render the trainee_dashboard.html template with the context data
    return render(request, 'trainee_dashboard.html', context)

def workout_plan_view(request):
    user=request.user
    workout_plan = WorkoutPlan.objects.filter(trainee=user).first()# Get the workout plan from the databas
    return render(request, 'workout_plan.html',{'workout_plan': workout_plan})
def diet_plan_view(request):
    
    user=request.user
    diet_plan = DietPlan.objects.filter(trainee=user).first()  # You may need to adjust this depending on your model structure
    return render(request, 'diet_plan.html', {'diet_plan': diet_plan})

def calculate_total(cart_products):
    total = 0
    for product in cart_products:
        total += product.get('price', 0)  # Assuming each product has a 'price' key
    return total
def store_view(request):

    if request.method == 'POST':
        # Handle form submission or other POST requests here if needed
        pass
    else:
        # Retrieve products from the cart (assuming they are stored in session)
        cart_products = request.session.get('cart', [])
        
        # Calculate the total value of the products in the cart
        total_value = calculate_total(cart_products)
        
        # Construct the URL for the checkout page with cart products and total value
        checkout_url = reverse('checkout') + f'?cart={json.dumps(cart_products)}&total={total_value}'

        # Render the store.html template with any necessary context data
        return render(request, 'store.html', {'checkout_url': checkout_url})

def checkout_view(request):
    print('Get Parameters: ',request.GET)
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        # If user is not authenticated, redirect to the login page
        messages.info(request, 'Login To Continue.')
        return redirect('login')  
    
    if request.method == 'POST':
        user = request.user
        name = request.POST['name']
        phone_number = request.POST['phno']
        flat_block_no = request.POST['flatno']
        pincode = request.POST['pincode']
        address = request.POST['ad']
        state = request.POST['state']
        city_district = request.POST['city']
        locality = request.POST['landmark']
        alternate_phone_number = request.POST['aphno']
        
        # Create a new Shipment object and save it to the database
        shipment = Shipment.objects.create(
            user=user,
            name=name,
            phone_number=phone_number,
            flat_block_no=flat_block_no,
            pincode=pincode,
            address=address,
            state=state,
            city_district=city_district,
            locality=locality,
            alternate_phone_number=alternate_phone_number
        )
        shipment.save()
        # Redirect to a success page
        # return redirect('order_confirmation')  # You need to define 'order_confirmation' in your urls.py
    
    # If the request method is GET, render the checkout page
    # products_json = request.GET.get('cart', '')
    # total_value = request.GET.get('total', '')
    # products = json.loads(products_json)
    return render(request, 'checkout.html')


    