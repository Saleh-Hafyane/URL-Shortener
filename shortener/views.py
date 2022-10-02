from django.shortcuts import render,redirect
from django.http import HttpResponse
import uuid
from .models import Url
# Create your views here.
def index(req):
    return render(req,'index.html')

def create(req):
    if req.method == 'POST':
        bUrl = req.POST['link']
        shUrl = str(uuid.uuid4())[:5]
        url = Url(bLink=bUrl,shLink=shUrl)
        url.save()
        return HttpResponse(shUrl)
def unlink(req,pk):
    unlinkedUrl = Url.objects.get(shLink=pk)
    return redirect(unlinkedUrl.bLink)
