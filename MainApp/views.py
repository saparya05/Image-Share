from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def gallery(request):

    category = request.GET.get("category")
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    try:
        category = Category.objects.all()
    except Category.DoesNotExist:
        category = None


    context = {"category":category, "photos":photos}
    return render(request, 'gallery.html', context)


def viewImg(request, pk):
    try:
        photos = Photo.objects.get(id=pk)
    except Category.DoesNotExist:
        photos = None

    context = {"photos":photos}
    
    return render(request, 'view_img.html', context)



def addImg(request):
    try:
        categories = Category.objects.all()
    except Category.DoesNotExist:
        categories = None

    if request.method == "POST":
        data = request.POST

        if 'images' in request.FILES:

            image = request.FILES['images']

            if data['category'] != 'none':
                category = Category.objects.get(id=data['category'])

            elif data['category_new'] != '':
                category, created = Category.objects.get_or_create(name=data['category_new'])

            else:
                category = None

            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                photo=image,
            )
            return redirect('gallery')

    context = {"categories": categories}
    return render(request, 'add_img.html', context)