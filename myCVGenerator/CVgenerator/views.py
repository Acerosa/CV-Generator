from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
import pdfkit
from django.template import loader
import io
# Create your views here.


def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        summary = request.POST.get('summary', '')
        degree = request.POST.get('degree', '')
        school = request.POST.get('school', '')
        university = request.POST.get('university', '')
        previous_work = request.POST.get('previous_work', '')
        skills = request.POST.get('skills', '')
        profile = Profile(name=name,
                          email=email,
                          summary=summary,
                          degree=degree,
                          school=school,
                          university=university,
                          previous_work=previous_work,
                          skills=skills)
        profile.save()
    return render(request, 'CVgenerator/accept.html')


def cv(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('CVgenerator/cv.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page_size':'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    fileFame  = user_profile.name + 'cv.pdf'
    return response