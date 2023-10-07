from django.shortcuts import render
from django.views import View


class Index(View):
    templates_name = 'main_menu/main.html'

    def get(self, request):
        context = {
            'title': "Головна сторінка"
        }

        return render(request=request, context=context, template_name=self.templates_name)
