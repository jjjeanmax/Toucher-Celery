from drf_yasg import openapi

from ..serializers import ClientSerializer


client_get_schema = {
    'operation_summary': "Получение всех Клиентов",
    'security': [None],
    'responses': {
        200: openapi.Response('Получение всех Клиентов', ClientSerializer(many=True)),
        400: openapi.Response('Ошибка входных данных'),
        403: openapi.Response('Ошибка доступа'),
        404: openapi.Response('Заявка не найдена'),
    },
}

client_post_schema = {
    'operation_summary': "Создание Клиентов",
    'security': [None],
    'responses': {
        201: openapi.Response('Создание Клиентов', ClientSerializer(many=True)),
        400: openapi.Response('Ошибка входных данных'),
        403: openapi.Response('Клиент уже существует'),
    },
}