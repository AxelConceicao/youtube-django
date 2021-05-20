from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.base import ContentFile
# from django.contrib.auth.models import User
from authentication.models import User

import json
import base64
from uuid import UUID
from . import forms
from .models import Video

def is_valid_uuid(uuid_to_test):
  try:
    uuid_obj = UUID(uuid_to_test)
  except ValueError:
    return False
  return str(uuid_obj) == uuid_to_test

def searchView(request, search):
  context = {
    'search': search,
    'videos': Video.objects.filter(title__contains=search)
  }
  return render(request, "search.html", context)

def index(request):
  search = request.GET.get('search')
  if search is not None:
    return searchView(request, search)
  videos = Video.objects.order_by('-views')[:20]
  context = {
    'videos': videos
  }
  return render(request, "index.html", context)

def watch(request, id=''):
  if id == '':
    return redirect('video:index')
  context = {}
  if is_valid_uuid(id):
    videos = Video.objects.filter(id=id)
    video = None
    if len(videos) > 0:
      video = videos[0]
    if video:
      video.views += 1
      video.save()
      context['video'] = video
      context['liked'] = video.likes.filter(username=request.user.username).exists()
      context['disliked'] = video.dislikes.filter(username=request.user.username).exists()
    else:
      context['error'] = id
  else:
    context['error'] = id
  context['suggestions'] = Video.objects.order_by('?')[:10]
  return render(request, "watch.html", context)

def upload(request):
  if not request.user.is_authenticated:
    return redirect('authentication:login')
  if request.method == "POST":
    my_form = forms.UploadFileForm(request.POST or None, request.FILES or None)
    if my_form.is_valid():
      video = my_form.save()
      video.author = request.user
      video.save()
      return HttpResponse(json.dumps({"id": str(video.id), "url": video.file.url}), content_type="application/json")
  else:
    my_form = forms.UploadFileForm
  context = {
    "form": my_form,
  }
  return render(request, "upload.html", context)

# base64 image in ImageField : https://stackoverflow.com/a/48019221/10950805
def save_thumbnail(request):
  if request.method == "POST":
    json_data = json.loads(request.body)
    video_id = json_data['id']
    image_data = json_data['thumbnail']
    video = Video.objects.filter(id=video_id)[0]
    format, imgstr = image_data.split(';base64,')
    ext = format.split('/')[-1]
    data = ContentFile(base64.b64decode(imgstr))  
    file_name = str(video.id) + '.' + ext
    video.thumbnail.save(file_name, data, save=True)
    return HttpResponse('Thumbnail generated')

def like(request, id=''):
  if id == '':
    return redirect('video:index')
  if not request.user.is_authenticated:
    return redirect('authentication:login')
  videos = Video.objects.filter(id=id)
  video = None
  if len(videos) > 0:
    video = videos[0]
    if not video.likes.filter(username=request.user.username).exists():
      if video.dislikes.filter(username=request.user.username).exists():
        video.dislikes.remove(request.user)
      video.likes.add(request.user) # liked
    else:
      video.likes.remove(request.user) # nothing
    video.views -= 1
    video.save()
  return redirect('video:watch', id=id)

def dislike(request, id=''):
  if id == '':
    return redirect('video:index')
  if not request.user.is_authenticated:
    return redirect('authentication:login')
  videos = Video.objects.filter(id=id)
  video = None
  if len(videos) > 0:
    video = videos[0]
    if not video.dislikes.filter(username=request.user.username).exists():
      if video.likes.filter(username=request.user.username).exists():
        video.likes.remove(request.user)
      video.dislikes.add(request.user) # disliked
    else:
      video.dislikes.remove(request.user) # nothing
    video.views -= 1
    video.save()
  return redirect('video:watch', id=id)

def channel(request, username=''):
  if username == '':
    return redirect('video:index')
  context = {}
  users = User.objects.filter(username=username)
  if len(users) > 0:
    user = users[0]
    if user:
      context['channel'] = user
      context['videos'] = Video.objects.order_by('-views')
      context['subscribed'] = user.subscribers.filter(username=request.user.username).exists()
    else:
      context['error'] = username
  else:
    context['error'] = username
  return render(request, "channel.html", context)

def subscribe(request, username=''):
  if username == '':
    return redirect('video:index')
  if not request.user.is_authenticated:
    return redirect('authentication:login')
  users = User.objects.filter(username=username)
  if len(users) > 0:
    user = users[0]
    if not user.subscribers.filter(username=request.user.username).exists():
      user.subscribers.add(request.user)
      user.save()
  return redirect('video:channel', username=username)

def unsubscribe(request, username=''):
  if username == '':
    return redirect('video:index')
  if not request.user.is_authenticated:
    return redirect('authentication:login')
  users = User.objects.filter(username=username)
  if len(users) > 0:
    user = users[0]
    if user.subscribers.filter(username=request.user.username).exists():
      user.subscribers.remove(request.user)
      user.save()
  return redirect('video:channel', username=username)
