from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import get_random_text
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from .forms import TemplateForm, AuthenticationForm, AuthenticationFormRusError, CustomUserCreationForm


# def template_view(request):
#     if request.method == "GET":
#         return render(request, 'app/template_form.html')
#
#     if request.method == "POST":
#         received_data = request.POST  # Приняли данные в словарь
#
#         # как пример получение данных по ключу `my_text`
#         # my_text = received_data.get('my_text')
#         return JsonResponse(data=
#                             {
#                                 "my_name": received_data.get("my_text"),
#                                 "my_password": received_data.get("my_password"),
#                                 "my_email": received_data.get("my_email"),
#                                 "my_date": received_data.get("my_date"),
#                                 "my_number": received_data.get("my_number"),
#                                 "my_agreement": received_data.get("my_checkbox"),
#                                 "my_Py_lvl": received_data.get("my_select"),
#                                 "about_me": received_data.get("my_textarea"),
#                             }, json_dumps_params={"ensure_ascii": False, "indent": 4})

def template_view(request):
    if request.method == "GET":
        return render(request, 'app/template_form.html')

    if request.method == "POST":
        received_data = request.POST  # Приняли данные в словарь
        form = TemplateForm(received_data)
        if form.is_valid():
            # my_text = form.cleaned_data.get("my_text")  # Получили очищенные данные
            # my_password = form.cleaned_data.get("my_password")
            # my_email = form.cleaned_data.get("my_email")
            # my_date = form.cleaned_data.get("my_date")
            # my_number = form.cleaned_data.get("my_number")
            # my_checkbox = form.cleaned_data.get("my_checkbox")
            # my_select = form.cleaned_data.get("my_select")
            # my_textarea = form.cleaned_data.get("my_textarea")
            return JsonResponse(data=form.cleaned_data, json_dumps_params={"indent": 4,
                                                                           "ensure_ascii": False})
        return render(request, 'app/template_form.html', context={"form": form})


# def login_view(request):
#     if request.method == "GET":
#         return render(request, 'app/login.html')
#
#     if request.method == "POST":
#         data = request.POST
#         user = authenticate(username=data["username"], password=data["password"])
#         if user:
#             login(request, user)
#             return redirect("app:user_profile")
#         return render(request, "app/login.html", context={"error": "Неверные данные"})
def login_view(request):
    if request.method == "GET":
        return render(request, 'app/login.html')

    if request.method == "POST":
        data = request.POST
        form = AuthenticationFormRusError(request, data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("app:user_profile")
        return render(request, "app/login.html", context={"form": form})


def logout_view(request):
    if request.method == "GET":
        logout(request)
        return redirect("/")


def register_view(request):
    if request.method == "GET":
        return render(request, 'app/register.html')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Возвращает сохраненного пользователя из данных формы
            login(request, user)
            return redirect("app:user_profile")

        return render(request, 'app/register.html', context={"form": form})


def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("app:user_profile")
        return render(request, 'app/index.html')


def user_detail_view(request):
    if request.method == "GET":
        return render(request, 'app/user_details.html')


def get_text_json(request):
    if request.method == "GET":
        return JsonResponse({"text": get_random_text()},
                            json_dumps_params={"ensure_ascii": False})
