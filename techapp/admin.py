from django.contrib import admin
from .models import TestimonialSection
from .models import LogoScrollSection
from .models import FaqSection

# Register your models here.
class TestimonialSectionAdmin(admin.ModelAdmin):
    list_display = ('name','profession','comment','avatar','youtube')

class LogoScrollSectionAdmin(admin.ModelAdmin):
    list_display = ('company','logo')

class FaqSectionAdmin(admin.ModelAdmin):
    list_display = ('question','answer')

admin.site.register(TestimonialSection,TestimonialSectionAdmin)
admin.site.register(LogoScrollSection,LogoScrollSectionAdmin)
admin.site.register(FaqSection,FaqSectionAdmin)