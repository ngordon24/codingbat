from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


# Create your views here.
def nearest_hundred(request: HttpRequest, num: int) -> HttpResponse:
    number = num
    if number + 10 >= 100:
        return HttpResponse("True")
    elif number + 10 >= 200:
        return HttpResponse("True")
    else:
        return HttpResponse("False")


def string_splosion(request: HttpRequest, string: str) -> HttpResponse:
    result = ""
    for i in range(len(string)):
        result += string[: i + 1]
    return HttpResponse(result)


def cat_dog(request: HttpRequest, string: str) -> HttpResponse:
    cat_count = string.count("cat")
    dog_count = string.count("dog")
    return HttpResponse(cat_count == dog_count)


def lone_sum(request: HttpRequest, num1: int, num2: int, num3: int) -> HttpResponse:
    if num1 == num2 and num2 == num3:
        return HttpResponse(0)
    elif num1 == num3:
        return HttpResponse(num2)
    elif num2 == num3:
        return HttpResponse(num1)
    elif num2 == num1:
        return HttpResponse(num3)
    else:
        return HttpResponse(num1 + num2 + num3)
