from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import numpy as np
import urllib
import json
import cv2
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from .forms import UploadImageForm
from .forms import ImageUploadForm
# import our OCR function
from .ocr import ocr

def first_view(request):
    return render(request, 'pcard/first_view.html', {})

def uimage(request):
  if request.method == 'POST':
      form = UploadImageForm(request.POST, request.FILES)
      if form.is_valid():
          myfile = request.FILES['image']
          fs = FileSystemStorage()
          filename = fs.save(myfile.name, myfile)
          uploaded_file_url = fs.url(filename)
      return render(request, 'pcard/uimage.html', {'form': form, 'uploaded_file_url': uploaded_file_url})
  
  else:
      form = UploadImageForm()
      return render(request, 'pcard/uimage.html', {'form': form})

def ocr_core(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
 
            imageURL = settings.MEDIA_URL + form.instance.image.name
            extracted_text = ocr(settings.MEDIA_ROOT_URL + imageURL)
 
            return render(request, 'pcard/pcard.html', {'form':form, 'post':post, 'extracted_text': extracted_text, 'img_src' : imageURL})
    else:
        form = ImageUploadForm()
    return render(request, 'pcard/pcard.html',{'form':form})