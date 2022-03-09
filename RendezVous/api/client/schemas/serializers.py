from drf_yasg import openapi

client_serializer_schema = {
    'properties': {
        'id': openapi.Schema(
            title='Идентификатор бекенда',
            type=openapi.TYPE_INTEGER,
        ),
        'phone_number': openapi.Schema(
            title='номер телефона',
            type=openapi.TYPE_STRING,
        ),
        'email': openapi.Schema(
            title='email',
            type=openapi.FORMAT_EMAIL,
        ),
        'email_confirmed': openapi.Schema(
            title='подтверждена ли почта',
            type=openapi.TYPE_BOOLEAN,
        ),
        'last_name': openapi.Schema(
            title='фамилия',
            type=openapi.TYPE_STRING,
        ),
        'first_name': openapi.Schema(
            title='имя',
            type=openapi.TYPE_STRING,
        ),
    },
    'example': [
        {
            'id': 1,
            'phone_number': '+7800000000',
            'email': 'm@mail.ru',
            'email_confirmed': False,
            'last_name': 'tu',
            'first_name': 'mapel',
        },
        {
            'id': 2,
            'phone_number': '+70000000000',
            'email': 'j@mail.ru',
            'email_confirmed': True,
            'last_name': 'je',
            'first_name': 'mapel',
        }
    ],
    'required': ['email', 'phone_number'],
}
