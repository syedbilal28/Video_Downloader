from django.shortcuts import render
from urllib.parse import urlparse
from. import Instagram_Images,Instagram_Videos,Facebook,TwitterVideoScrapper
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
def first_page(request):
    return render(request,"landing_page.html")
def index(request):
    url=request.POST['link']
    print(url)
    url_parsed = urlparse(url)
    print(url_parsed)
    domain = url_parsed.netloc
    path = url_parsed.path
    if "instagram" in path:
        fetch = Instagram_Images.application(url, path)
        if fetch == 0:
            fetch = Instagram_Videos.application(url, path)
    if "facebook" in path:
        fetch = Facebook.application(url, path)
    if "twitter" in path:
        fetch= TwitterVideoScrapper.TwitterDownloader(url,"D:/Twitter",1).download()
    return HttpResponse("hello")