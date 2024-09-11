from django.shortcuts import render
from .models import TestimonialSection
from .models import LogoScrollSection
from .models import FaqSection
from .models import CourseDetailsSection
from .models import ServiceDetailsSection

# Create your views here.
def index(request):
    testimonialSection = TestimonialSection.objects.all()
    logoScrollSection = LogoScrollSection.objects.all()
    faqSection = FaqSection.objects.all()
    courseDetailsSection = CourseDetailsSection.objects.all()
    serviceDetailsSection = ServiceDetailsSection.objects.all()
    return render(request, 'index.html',{
        'testimonialSection' :testimonialSection,
        'logoScrollSection' :logoScrollSection,
        'faqsection' :faqSection,
        'courseDetailsSection' :courseDetailsSection,
        'serviceDetailsSection' :serviceDetailsSection,
    })

def about(request):
    logoScrollSection = LogoScrollSection.objects.all()
    faqSection = FaqSection.objects.all()
    return render(request, 'about.html',{
        'logoScrollSection' :logoScrollSection,
        'faqsection' :faqSection,
    })

def courses(request):
    logoScrollSection = LogoScrollSection.objects.all()
    faqSection = FaqSection.objects.all()
    courseDetailsSection = CourseDetailsSection.objects.all()
    serviceDetailsSection = ServiceDetailsSection.objects.all()
    return render(request, 'courses.html',{
        'logoScrollSection' :logoScrollSection,
        'faqsection' :faqSection,
        'courseDetailsSection' :courseDetailsSection,
        'serviceDetailsSection' :serviceDetailsSection,
    })

def testimonial(request):
    testimonialSection = TestimonialSection.objects.all()
    logoScrollSection = LogoScrollSection.objects.all()
    faqSection = FaqSection.objects.all()
    return render(request, 'testimonial.html',{
        'testimonialSection' :testimonialSection,
        'logoScrollSection' :logoScrollSection,
        'faqsection' :faqSection,
    })

def course01(request):
    logoScrollSection = LogoScrollSection.objects.all()
    faqSection = FaqSection.objects.all()
    courseDetailsSection = CourseDetailsSection.objects.all()
    serviceDetailsSection = ServiceDetailsSection.objects.all()
    return render(request, 'course01.html',{
        'logoScrollSection' :logoScrollSection,
        'faqsection' :faqSection,
        'courseDetailsSection' :courseDetailsSection,
        'serviceDetailsSection' :serviceDetailsSection,
    })

def course02(request):
    logoScrollSection = LogoScrollSection.objects.all()
    faqSection = FaqSection.objects.all()
    courseDetailsSection = CourseDetailsSection.objects.all()
    serviceDetailsSection = ServiceDetailsSection.objects.all()
    return render(request, 'course02.html',{
        'logoScrollSection' :logoScrollSection,
        'faqsection' :faqSection,
        'courseDetailsSection' :courseDetailsSection,
        'serviceDetailsSection' :serviceDetailsSection,
    })

def course03(request):
    logoScrollSection = LogoScrollSection.objects.all()
    faqSection = FaqSection.objects.all()
    courseDetailsSection = CourseDetailsSection.objects.all()
    serviceDetailsSection = ServiceDetailsSection.objects.all()
    return render(request, 'course03.html',{
        'logoScrollSection' :logoScrollSection,
        'faqsection' :faqSection,
        'courseDetailsSection' :courseDetailsSection,
        'serviceDetailsSection' :serviceDetailsSection,
    })

def course04(request):
    logoScrollSection = LogoScrollSection.objects.all()
    faqSection = FaqSection.objects.all()
    courseDetailsSection = CourseDetailsSection.objects.all()
    serviceDetailsSection = ServiceDetailsSection.objects.all()
    return render(request, 'course04.html',{
        'logoScrollSection' :logoScrollSection,
        'faqsection' :faqSection,
        'courseDetailsSection' :courseDetailsSection,
        'serviceDetailsSection' :serviceDetailsSection,
    })

def course05(request):
    logoScrollSection = LogoScrollSection.objects.all()
    faqSection = FaqSection.objects.all()
    courseDetailsSection = CourseDetailsSection.objects.all()
    serviceDetailsSection = ServiceDetailsSection.objects.all()
    return render(request, 'course05.html',{
        'logoScrollSection' :logoScrollSection,
        'faqsection' :faqSection,
        'courseDetailsSection' :courseDetailsSection,
        'serviceDetailsSection' :serviceDetailsSection,
    })

def course06(request):
    logoScrollSection = LogoScrollSection.objects.all()
    faqSection = FaqSection.objects.all()
    courseDetailsSection = CourseDetailsSection.objects.all()
    serviceDetailsSection = ServiceDetailsSection.objects.all()
    return render(request, 'course06.html',{
        'logoScrollSection' :logoScrollSection,
        'faqsection' :faqSection,
        'courseDetailsSection' :courseDetailsSection,
        'serviceDetailsSection' :serviceDetailsSection,
    })