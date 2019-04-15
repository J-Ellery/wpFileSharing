from django.shortcuts import render
#from django.http import HttpResponse
from .models import Academic_dept, Academic_class, Upload
from django.shortcuts import get_object_or_404, render


def index(request):
    dept_list = Academic_dept.objects.order_by('-dept_code')
    context = {'dept_list': dept_list}
    return render(request, 'wpFiles/index.html', context)
          
def classInDept(request, dept_id):
    dept = get_object_or_404(Academic_dept, pk=dept_id)
    return render(request, 'wpFiles/classInDept.html', {'dept': dept})
    
def uploads(request, class_id):
    academic_class = get_object_or_404(Academic_class, pk=class_id)
    return render(request, 'wpFiles/uploads.html', {'academic_class': academic_class})
    
   
