
>>> from tags.models import Tag
>>> Tag.object.all()

>>> Tag.objects.all()
<QuerySet [<Tag: T shirt>, <Tag: Tshirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Blac
k>]>
>>> Tag.objects.last()
<Tag: Black>
>>> black =  Tag.objects.last()
>>> black.title
'Black'
>>> black.slug
'black'
>>> black.active
False
>>> black.products
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager
.<locals>.ManyRelatedManager object at 0x0000000003EFF2B0>
>>> black.products.all()
<ProductQuerySet [<Product: T-shirt>, <Product: Hat>, <Product: T-shirt>]>

>>> black.products.all().last()
<Product: T-shirt>
>>> black.products.all().first()
<Product: T-shirt>

(cart) C:\Users\Mr. Isaac\Desktop\tryFive\cart\product>python manage.py shell
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bi
t (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.models import Product
>>> qs = Products.objects.all
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Products' is not defined
>>> qs = Product.objects.all()
>>> qs
<ProductQuerySet [<Product: T-shirt>, <Product: Hat>, <Product: supercomputers>,
 <Product: T-shirt>, <Product: Loren>]>
>>> t-shirt = qs.first()
  File "<console>", line 1
SyntaxError: can't assign to operator
>>> tshirt = qs.first()
>>> tshirt
<Product: T-shirt>
>>> tshirt.title
'T-shirt'
>>> tshirt.description
'This is an awesome T-shirt'
>>> tshirt.tag

>>> tshirt.tag_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager
.<locals>.ManyRelatedManager object at 0x0000000003F25780>
>>> tshirt.tag_set.all()
<QuerySet [<Tag: T shirt>, <Tag: Tshirt>, <Tag: T-shirt>, <Tag: Red>, <Tag: Blac
k>]>
>>> tshirt.tag_set.filter(title__iexact='Black')
<QuerySet [<Tag: Black>]>