from django.shortcuts import render, redirect,reverse

from .models import Photo
from .forms import PhotoForm


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('cropper:photo_list'))
    else:
        form = PhotoForm()
    return render(request, 'cropper/index.html', {'form': form, 'photos': photos})