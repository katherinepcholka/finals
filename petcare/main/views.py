from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Product, Category


class MainPage(ListView):
    template_name = 'main/main_page.html'
    context_object_name = 'new_goods'

    def get_queryset(self):
        return Product.available.all().order_by('-id')[:4] 

def about(request):
    return render(request, 'main/about.html')

class ProductByCategory(ListView):
    model = Product
    template_name = 'goods/product_list.html'
    context_object_name = 'products'
    category = None
    paginate_by = 6


    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        self.sub_categories=self.category.get_descendants(include_self=True)
        queryset = Product.available.all().filter(category__in=self.sub_categories)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = f'Продукты категории: {self.category.name}'
        return context


class ShowProduct(DetailView):
    model = Product
    template_name = 'goods/product.html'
    pk_url_kwarg = 'prdt_id'
    context_object_name = 'product'


class Search(ListView):
    template_name = 'goods/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.available.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
