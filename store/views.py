from django.shortcuts import render
from django.views import View


class Index(View):
    templates_name = 'main_menu/main.html'

    def get(self, request):
        context = {
            'title': "Головна сторінка"
        }

        return render(request=request, context=context, template_name=self.templates_name)


class About(View):
    templates_name = r'main_menu/about.html'

    def get(self, request):
        context = {
            'title': 'About'
        }

        return render(request=request, context=context, template_name=self.templates_name)

class Contact(View):
    templates_name = r'main_menu/contact.html'

    def get(self, request):
        context = {
            'title': 'Контакти'
        }
        return render(request=request, context=context, template_name=self.templates_name)

