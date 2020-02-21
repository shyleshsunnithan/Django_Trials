from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
def blog(request):
    return HttpResponse("<h1>Hi There</h1>")

def kope(request):
    return JsonResponse({"hello " : "<h1>Hope You Are Good/h1>"})

def portfolio(request):
    return render(request,"test.html",{"resume":[{"name":"Shylesh","lname":"Unnithan","age":"19","skills":["Python","Python Django","C++"],"exp":["Intern at Spider Innovative","ECC, IEEE Kochi Hub","Vice-Chairman, CS Chapter IEEE SB CEC"]},
    {"name":"Saranya","lname":"V Unnithan","age":"24","skills":["Speaking","Speech","C++"],"exp":["Intern at Incubation","Former Sports Captain KV Adoor"]}, {"name":"Rithu Maria","lname":"Jose","age":"19","skills":["Public Speaking","Speech","C++"],"exp":["Intern at Innostack","Kochi Hub Coordinator, CS Chapter IEEE Kerala Section","Vie Chairperson, WIE AG IEEE SB CEC"]}]})

def test(request):
    print(request.GET)
