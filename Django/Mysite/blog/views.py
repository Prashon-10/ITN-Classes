
from importlib.resources import contents
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages


from .models import Student


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        Student.objects.create(
            name=name, email=email, address=address, phone=phone)
        messages.success(request, "Data was Insterted.")
        return redirect("index")

    else:
        content = {
            "studentData": Student.objects.all()
        }
        return render(request, "index.html", content)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def delete(request, id):
    Student.objects.get(id=id).delete()
    messages.success(request, "Data was deleted.")
    return redirect("index")


def edit(request, id):
    if request.method == "POST":
        obj = Student.objects.get(id=id)
        obj.name = request.POST['name']
        obj.email = request.POST['email']
        obj.address = request.POST['address']
        obj.phone = request.POST['phone']
        obj.save()

        messages.success(request, "Data was Updated.")
        return redirect("index")

    else:
        content = {
            "studentData": Student.objects.get(id=id)
        }
        return render(request, "update.html", content)


# def service(request):
#     return render(request, "services.html")
