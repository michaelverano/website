from django.shortcuts import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('resume/index.html')
    return HttpResponse(template.render({}, request))

