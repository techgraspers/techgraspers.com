from django.contrib import admin
from .models import TestimonialSection
from .models import LogoScrollSection
from .models import FaqSection
from .models import CourseDetailsSection
from .models import ServiceDetailsSection

# Register your models here.
class TestimonialSectionAdmin(admin.ModelAdmin):
    list_display = ('name','profession','comment','avatar','youtube')

class LogoScrollSectionAdmin(admin.ModelAdmin):
    list_display = ('company','logo')

class FaqSectionAdmin(admin.ModelAdmin):
    list_display = ('question','answer')

class CourseDetailsSectionAdmin(admin.ModelAdmin):
    list_display = ('title','description','page_link','button_link','image')

class ServiceDetailsSectionAdmin(admin.ModelAdmin):
    list_display = ('title','description','popup_link','button_link','image','heading','description_popup','second_heading','list_01','list_01_desc','list_02','list_02_desc','list_03','list_03_desc')

admin.site.register(TestimonialSection,TestimonialSectionAdmin)
admin.site.register(LogoScrollSection,LogoScrollSectionAdmin)
admin.site.register(FaqSection,FaqSectionAdmin)
admin.site.register(CourseDetailsSection,CourseDetailsSectionAdmin)
admin.site.register(ServiceDetailsSection,ServiceDetailsSectionAdmin)