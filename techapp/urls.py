from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="techapp"),
    path('about/',views.about, name="about"),
    path('courses/',views.courses, name="courses"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('course01/', views.course01, name="course01"),
    path('course02/', views.course02, name="course02"),
    path('course03/', views.course03, name="course03"),
    path('course04/', views.course04, name="course04"),
    path('course05/', views.course05, name="course05"),
    path('course06/', views.course06, name="course06"),
]