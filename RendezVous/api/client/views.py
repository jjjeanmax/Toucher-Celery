from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from .serializers import ClientSerializer
from .schemas.methods import client_get_schema, client_post_schema
from .utils import generate_token

from core.tasks import async_send_email_task
from client.models import ClientProfile


class ClientView(APIView):
    """
    Получить/Создать
    """

    @staticmethod
    @swagger_auto_schema(**client_get_schema)
    def get(request):
        queryset = ClientProfile.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    @swagger_auto_schema(**client_post_schema)
    def post(request):
        serializer = ClientSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        client = ClientProfile.objects.create(
            phone_number=serializer.validated_data['phone_number'],
            email=serializer.validated_data['email'],
            last_name=serializer.validated_data['last_name'],
            first_name=serializer.validated_data['first_name'],
        )
        current_site = get_current_site(request)
        message = render_to_string('auth/activate.html',
                                   {
                                       'user': client,
                                       'domain': current_site.domain,
                                       'uid': urlsafe_base64_encode(force_bytes(client.pk)),
                                       'token': generate_token.make_token(client)
                                   }
                                   )
        email = serializer.validated_data['email']
        async_send_email_task.delay(email, message)
        messages.add_message(request, messages.SUCCESS,
                             'account created succesfully')
        return Response(status=status.HTTP_201_CREATED, data=ClientSerializer(client).data)


class ActivateAccountView(APIView):
    @staticmethod
    @swagger_auto_schema(**client_get_schema)
    def get(request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = ClientProfile.objects.get(pk=uid)

        except Exception as identifier:
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.email_confirmed = True
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 'account activated successfully')

            # TODO: LE TALON A RETOURNER
            # return redirect('talon')
            qs = ClientProfile.objects.filter(email_confirmed=True)
            serializer = ClientSerializer(qs, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return render(request, 'auth/activate_failed.html', status=401)


class TalonView():
    pass
