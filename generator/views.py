from django.shortcuts import render
from django.http import HttpResponse #нужно для возврата в нужном формате данных
import random
def home(request):
    return render(request,"generator/home.html") #упрощаем делая без шаблона
def about(request):
    return render(request, "generator/about.html", {"author_name": "ABLoktev","create_date":"20_05_2020"})  # упрощаем делая без шаблона


    #return render(request,"generator/home.html", {"password": "OLOLOLO"}) #берет из указанной папки шаблон странички и размещает его на сайте
    #секция {"password": "OLOLOLO"} позволяет использовать шаблоны в файле generator/home.html как в jinja2
    #return HttpResponse('Hello THERE FRINED') #то что будет отображено на страничке http://127.0.0.1:8000/
def password(request):
    #порой требуется перезагрузить сервер,чтобы все заработало
    characters = list("qwertyuiopasdfghjklzxcvbnm")
    if request.GET.get("uppercase"):
        characters.extend(list("QWERTYUI"))
    if request.GET.get("special"):
        characters.extend(list(",.*%:?>"))
    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))
        print("OLOLO")

    length = int(request.GET.get("length","13")) #<select name="length"> берется отсюда на странице home.html, "13" предоставляет нам дефолтное значение здесь,это не обязательно,но знак хорошего тона

    thepassword = ""
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request,"generator/password.html", {"password":thepassword}) #из словаря берется значение и помещается на страничку в поле {{password}}

    #return render(request,"generator/home.html", {"password": "OLOLOLO"}) #берет из указанной папки шаблон странички и размещает его на сайте
#можно сипользовать html тегирование
