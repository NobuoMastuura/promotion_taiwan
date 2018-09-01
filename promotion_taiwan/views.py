from django.shortcuts import render
from django.views.generic import TemplateView


# # def index(requset):
#     return render(requset, 'promotion_taiwan/index.html')

class IndexTemplateView(TemplateView):
    template_name = "promotion_taiwan/index.html"
