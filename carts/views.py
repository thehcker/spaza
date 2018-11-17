from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Cart
from products.models import Product

# Create your views here.
@login_required
def cart_home(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	# products = cart_obj.products.all()
	# total = 0
	# for x in products:
	# 	total += x.price
	# print(total)
	# cart_obj.total = total
	# cart_obj.save()
	return render(request,"carts/home.html", {"cart":cart_obj})
@login_required
def cart_update(request):
	product_id = request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("Product is gone")
			return redirect("carts:cart")
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj)  # cart_obj.products.add(product_id)
		request.session['cart_items'] = cart_obj.products.count()	
	#cart_obj.products.add(product_obj)
	#return redirect(product_obj.get_absolute_url())
	return redirect("carts:cart")