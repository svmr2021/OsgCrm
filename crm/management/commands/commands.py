import fileinput
from django.core.management.base import BaseCommand
import json
import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve()

BASE_DIR = str(BASE_DIR)

print(BASE_DIR)

class Command(BaseCommand):
    help = 'Help information'

    def add_arguments(self, parser):
        parser.add_argument('dir', type=str, help='Project folder name should be string.')
        parser.add_argument('app', type=str, help='App name should be string.')
        parser.add_argument('model', type=str, help='Model name should be string.')

    def handle(self, *args, **options):
        dir = options['dir']
        app = options['app']
        model = options['model']

        if self.check_args(dir,app,model) is None:
            try:
                self.create_structure(app, dir, BASE_DIR)
            except:
                pass
            self.create_main_urls(model, app)
            self.create_serializer(app, model)
            self.create_view(app, model)
        else:
            print('Error occured')

    def check_args(self,dir,app,model):
        if dir in BASE_DIR:
            pass
        else:
            return 'Dir not found'

        try:
            __import__(app)
        except:
            return 'App not found'
        try:
            f = open(f'{app}/models.py','r')
            file = f.read()
            if model in file:
                return None
            else:
                return False
        except:
            return 'Model not found'

    def create_structure(self, app, dir, BASE_DIR):
        list = []
        temp = ''
        string = ''
        url = ''

        for i in BASE_DIR:
            if i != '/':
                temp += i
            else:
                if temp == dir:
                    string += temp + '/'
                    list.append(string)
                else:
                    string += temp + '/'
                    temp = ''

        BASE_DIR = list[0]
        parent_dir = ''
        try:
            directory = 'Api'
            parent_dir = BASE_DIR
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Structure exists...'))
        try:
            directory = 'v1'
            parent_dir = str(BASE_DIR) + '/Api'
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
        except Exception as e:
            pass

        try:
            directory = f'{app}'
            parent_dir += '/v1'
            path = os.path.join(parent_dir, directory)
            os.mkdir(path)
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Folder for {app} exists...'))

        try:
            url = str(BASE_DIR) + 'Api'
            j = open(f'{url}/__init__.py', 'x')
            j.close()

            f = open(f'{url}/urls.py', 'x')
            f.close()

            url += '/v1'
            l = open(f'{url}/__init__.py', 'x')
            l.close()

            h = open(f'{url}/urls.py', 'x')
            h.close()

            url += f'/{app}'
            s = open(f'{url}/serializers.py', 'x')
            u = open(f'{url}/urls.py', 'x')
            v = open(f'{url}/views.py', 'x')
            s.close()
            u.close()
            v.close()
        except Exception as e:
            pass

        try:
            url += f'/v1/{app}'
            s = open(f'{url}/serializers.py', 'x')
            u = open(f'{url}/urls.py', 'x')
            v = open(f'{url}/views.py', 'x')
            s.close()
            u.close()
            v.close()
        except Exception as e:
           pass

        try:
            self.create_urls(app)
        except Exception as e:
           pass

    def create_urls(self,app):
        importing = 'from django.urls import path, include\n\n\n'
        urls = 'urlpatterns'
        urlpatterns = "urlpatterns = [path('v1/', include('Api.v1.urls'))]\n"
        v1_urlpatterns =f"urlpatterns = [path('{app.lower()}/',include('Api.v1.{app}.urls'))]\n"
        app_path =f"[path('{app.lower()}/',include('Api.v1.{app}.urls'))]\n"
        try:
            f = open('Api/urls.py','r')
            k = open('Api/urls.py','a')
            file = f.read()
            if importing not in file:
                k.write(importing)
            if urlpatterns not in file:
                k.write(urlpatterns)
            f.close()
            k.close()
        except Exception as e:
            print(e)

        try:
            f = open(f'Api/v1/urls.py','r')
            k = open('Api/v1/urls.py','a')
            file = f.read()
            if importing not in file:
                k.write(importing)
            if urls not in file:
                k.write(v1_urlpatterns)
            elif app_path not in file:
                urlpt = 'urlpatterns += '
                urlpt +=app_path
                k.write(urlpt)
            f.close()
            k.close()
        except Exception as e:
            print(e)

    def create_serializer(self, app, model):
        importing = f'from rest_framework import serializers\n'
        import_model = f'from {app}.models import {model}\n\n\n'

        serializer = f'class {model}Serializer(serializers.ModelSerializer):\n' \
                     f'    class Meta:\n' \
                     f'        model = {model}\n' \
                     f'        fields = "__all__"\n\n\n'
        try:
            f = open(f'Api/v1/{app}/serializers.py', 'r')
            file = f.read()
            if importing not in file:
                f = open(f'Api/v1/{app}/serializers.py', 'a')
                f.write(importing)
                f.close()
            if not (import_model or serializer) in file:
                f = open(f'Api/v1/{app}/serializers.py', 'a')
                f.write(import_model)
                f.write(serializer)
                f.close()
                self.stdout.write(self.style.SUCCESS(f'Serializers created!'))
            elif import_model in file and not serializer in file:
                f = open(f"Api/v1/{app}/serializers.py", 'a')
                f.write(serializer)
                self.stdout.write(self.style.SUCCESS(f'Serializers created!'))
            elif serializer in file and not import_model in file:
                f = open(f"Api/v1/{app}/serializers.py", 'a')
                f.write(import_model)
                self.stdout.write(self.style.SUCCESS(f'Serializers created!'))
            else:
                self.stdout.write(self.style.ERROR(f'Serializer for "{model}" already exists!'))

        except:
            self.stdout.write(self.style.ERROR(f'Folder "{app}" not found'))

    def create_view(self, app, model):
        importing = f'from rest_framework.generics import * \n' \
                    f'from rest_framework.permissions import *\n' \
                    f'from Api.v1.{app}.serializers import *\n' \
                    f'from {app}.models import *\n\n\n'
        list_create = f'class {model}ListView(ListAPIView):\n' \
                      f'    serializer_class = {model}Serializer\n' \
                      f'    permission_classes = (AllowAny,)\n' \
                      f'    queryset = {model}.objects.all()\n\n\n' \
                      f'class {model}CreateView(CreateAPIView):\n' \
                      f'    serializer_class = {model}Serializer\n' \
                      f'    permission_classes = (IsAuthenticatedOrReadOnly,)\n' \
                      f'    queryset = {model}.objects.all()\n\n\n' \
                      f'class {model}EditView(RetrieveUpdateDestroyAPIView):\n' \
                      f'    serializer_class = {model}Serializer\n' \
                      f'    permission_classes = (IsAuthenticatedOrReadOnly,)\n' \
                      f'    queryset = {model}.objects.all()\n\n\n'
        try:
            f = open(f'Api/v1/{app}/views.py', 'r')
            file = f.read()
            if importing not in file:
                f = open(f'Api/v1/{app}/views.py', 'a')
                f.write(importing)
                f.close()
            if not list_create in file:
                f = open(f'Api/v1/{app}/views.py', 'a')
                f.write(list_create)
                f.close()
                self.stdout.write(self.style.SUCCESS(f'Views created!'))
            else:
                self.stdout.write(self.style.ERROR(f'Views for "{model}" already exists!'))
        except:
            pass

    def create_main_urls(self, model, app):
        importing = f'from django.urls import path\n' \
                    f'from Api.v1.{app}.views import *\n'
        urls = 'urlpatterns'
        urlpatterns = 'urlpatterns = []'
        list_path = f"path('{model.lower()}/list/',{model}ListView.as_view())"
        create_path = f"path('{model.lower()}/create/',{model}CreateView.as_view())"
        detail_path = f"path('{model.lower()}/detail/<int:pk>',{model}EditView.as_view())"

        k = open(f'Api/v1/{app}/urls.py', 'r')
        file = k.read()
        if importing not in file:
            k = open(f'Api/v1/{app}/urls.py', 'a')
            k.write(importing)
            k.close()
        try:
            if urls not in file:
                if list_path and detail_path not in file:
                    list = []
                    list.append(list_path)
                    list.append(create_path)
                    list.append(detail_path)

                    json_string = 'urlpatterns = '
                    json_string += json.dumps(list, indent=2)
                    json_string += '\n'

                    k = open(f'Api/v1/{app}/urls.py', 'a')
                    k.write(json_string.replace('"', ''))
                    k.close()
                    self.stdout.write(self.style.SUCCESS(f'Urls created!'))
                else:
                    self.stdout.write(self.style.ERROR(f'Urls for "{model}" already exists!'))
            else:
                if list_path and detail_path not in file:
                    list = []
                    list.append(list_path)
                    list.append(create_path)
                    list.append(detail_path)
                    json_string = 'urlpatterns += '
                    json_string += json.dumps(list, indent=2)
                    json_string += '\n'
                    if urlpatterns in file:
                        with fileinput.FileInput(f'Api/v1/{app}/urls.py', inplace=True) as file:
                            for line in file:
                                print(line.replace(urlpatterns, json_string.replace('"', '')), end='')
                    else:
                        k = open(f'Api/v1/{app}/urls.py', 'a')
                        k.write(json_string.replace('"', ''))
                        k.close()
                    self.stdout.write(self.style.SUCCESS(f'Urls created!'))
                else:
                    self.stdout.write(self.style.ERROR(f'Urls for "{model}" already exists!'))
        except Exception as e:
            print(e)
