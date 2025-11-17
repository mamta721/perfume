from django.shortcuts import render, redirect, HttpResponse
from .models import *  # Use proper imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User

def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')
        
        # Create order
        order = Order.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            payment_method=payment_method,
            total_items=cart_items.count(),
            total_amount=total_price
        )
        
        # Clear the cart after order
        cart_items.delete()
        
        return redirect(thankyou)
    
    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(fname=fname, lname=lname, email=email, message=message)  # Fixed model name
        return HttpResponse("Your Message Sent!")
    return render(request, 'contact.html')

# Keep your other views as they are...
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'index.html')
def buy_perfume(request):
    men_products=Product.objects.filter(category='Men')
    return render(request,'buy-perfume.html',{'men_products':men_products})

def contact(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        message=request.POST['message']
        Contact(fname=fname,lname=lname,email=email,message=message).save()
        return HttpResponse("Your Message Sent!")
    return render(request,'contact.html')
def men(request):
    men_products=Product.objects.filter(category='Men')
    return render(request,'men.html',{'men_products': men_products})
def women(request):
    women_products=Product.objects.filter(category='Women')
    return render(request,'women.html',{'women_products':women_products})
def exclusive(request):
    exclusive_products=Product.objects.filter(category='Exclusive')
    return render(request,'exclusive.html',{'exclusive_products':exclusive_products})
def exclusive1(request):
    return render(request,'exclusive1.html')
def cart(request):
    cart_items=CartItem.objects.filter(user=request.user)
    total_price=sum(item.product.price * item.quantity for item in cart_items)

    return render(request,'cart.html',{'cart_items':cart_items,'total_price':total_price})
@login_required
def product_details(request, id):
    x = Product.objects.get(id=id)

    if request.method == 'POST':
        qty = int(request.POST['quantity'])

        CartItem.objects.create(
            product=x,
            quantity=qty,
            user=request.user
        )
        return redirect(cart)   # Use a name, not the function

    return render(request, 'product_details.html', {'x': x})

def delt(request,id):
    d=CartItem.objects.get(id=id,user=request.user)
    d.delete()
    return redirect(cart)
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, 'signup.html')


# def checkout(request):
#     cart_items = CartItem.objects.filter(user=request.user)
#     total_price = sum(item.product.price * item.quantity for item in cart_items)

#     if request.method == "POST":
#         # You can process order here
#         # e.g., save shipping info, clear cart, send email, etc.
#         return redirect(thankyou)  # Create this page

#     return render(request, 'checkout.html', {
#         'cart_items': cart_items,
#         'total_price': total_price
#     })

def thankyou(request):
    if request.method == "POST":
        # Process order (save, clear cart, email, etc.)
        return redirect('thankyou')  # URL name for thankyou page
    return render(request,'thankyou.html')
