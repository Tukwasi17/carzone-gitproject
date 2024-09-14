from django.shortcuts import get_object_or_404, render
from cars.models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)#the paginator created
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    #for duplicate to be ignored
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)#getting from database
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)

def search(request):
    cars = Car.objects.order_by('-created_date')
    #for duplicate to be ignored
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:#if we have keyword in our browser then
        keyword = request.GET['keyword']#we take that keyword and store
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:#if we have keyword in our browser then
        model = request.GET['model']#we take that keyword and store
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:#if we have keyword in our browser then
        city = request.GET['city']#we take that keyword and store
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:#if we have keyword in our browser then
        year = request.GET['year']#we take that keyword and store
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:#if we have keyword in our browser then
        body_style = request.GET['body_style']#we take that keyword and store
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in  request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)#gte mean greater than, while lte is less than price                                       
    
    data = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_serach': transmission_search,
    }
    return render(request, 'cars/search.html', data)