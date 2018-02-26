from django.http import HttpResponse
from django.template import loader
from django.http import request


def index(request):
    template = loader.get_template('File_missing_report/index.html')
    return HttpResponse(template.render({}, request))
