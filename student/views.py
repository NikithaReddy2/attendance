from django.shortcuts import render,get_list_or_404,get_object_or_404
from student.forms import formName
from student.models import studentModel

# Create your views here.
def saved(request):
    return render(request,'saved.html')
def userForm(request):
    form = formName

    if request.method == 'POST':
       form = formName(request.POST)

       if form.is_valid:
           form.save()
           return saved(request)
       else:
           print('Form is not valid')

    return render(request,'users.html',{'form':form})


def display(request):
    stud = get_list_or_404(studentModel)
    return render(request,'display.html',{'stud':stud})


def update(request,num):
    stud = get_object_or_404(studentModel,id=num)

    if request.method == 'POST':
        a=request.POST
        stud.studentUsn = a['USN']
        stud.studentName = a['studentName']
        stud.sem = a['semester']
        stud.save()

        return display(request)

    return render(request,'update.html',{'stud':stud})


def delete(request,num):

    stud = get_object_or_404(studentModel,id=num)

    if request.method == 'POST':
        stud.delete()

        return display(request)

    return render(request,'delete.html')
