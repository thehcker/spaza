#from django.db.models import Q
from django.shortcuts import render
from products.models import Product

# Create your views here.
def search_product_view(request):
	method_dict = request.GET
	query = method_dict.get('q','Loren')
	queryset = Product.objects.search(query)
	context = {
		'object_list':queryset
	}
	template = 'search/view.html'
	return render(request,template,context)