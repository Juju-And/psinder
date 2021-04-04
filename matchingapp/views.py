# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the polls index.")