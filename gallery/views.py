from django.shortcuts import render, get_object_or_404
from .models import Gallery

def gallery_detail(request, gallery_id):
    gallery = get_object_or_404(Gallery, id=gallery_id)
    return render(request, 'gallery/gallery_detail.html', {'gallery': gallery})
