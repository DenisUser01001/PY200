from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from landing.forms import TemplateForm


class MyView(TemplateView):
    template_name = 'landing/index.html'  # Шаблон, который будет рендерится

    def post(self, request, *args, **kwargs):
        received_data = request.POST  # Приняли данные в словарь
        form = TemplateForm(received_data)  # Передали данные в форму

        if form.is_valid():  # Проверили, что данные все валидные

            # Заголовок HTTP_X_FORWARDED_FOR используется для идентификации исходного IP-адреса клиента,
            # который подключается к веб-серверу через HTTP-прокси или балансировщик нагрузки.
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')
            data = form.cleaned_data
            data['ip'] = ip
            data['user_agent'] = user_agent
            return JsonResponse(data=data, json_dumps_params={"indent": 4, "ensure_ascii": False})

        context = self.get_context_data(**kwargs)  # Получаем контекст, если он есть
        context["form"] = form  # Записываем в контекст форму
        return self.render_to_response(context)  # Возвращаем вызов метода render_to_response
