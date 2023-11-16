from django.shortcuts import render


def home(requests):
    return  render(requests,template_name='index.html')


def courses(requests):
    return render(requests, template_name='courses.html')