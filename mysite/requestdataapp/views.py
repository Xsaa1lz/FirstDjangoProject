from django.http import HttpRequest, HttpResponce
from django.shortcuts import render


def process_get_view(request: HttpRequest) -> HttpResponce:
    return render(request, "request-query-params.html", {})
