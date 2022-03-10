import time

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.http import FileResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.datetime_safe import datetime
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from Talon.models import Talon
from .serializers import ClientSerializer
from .schemas.methods import client_get_schema, client_post_schema
from .utils import generate_token, data

from core.tasks import async_send_email_task, async_render_to_pdf
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

        client, _ = ClientProfile.objects.get_or_create(
            phone_number=serializer.validated_data['phone_number'],
            email=serializer.validated_data['email'],
            last_name=serializer.validated_data['last_name'],
            first_name=serializer.validated_data['first_name'],
            created_at=serializer.validated_data['created_at'],

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
    """
    1 - send link to confirm email
    2 - after confirmed email user get Talon
    """

    @staticmethod
    @swagger_auto_schema(**client_get_schema)
    def get(request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = ClientProfile.objects.get(pk=uid)
            data['username'] = user.first_name + " " + user.last_name
            dt = user.created_at
            # Formatter datetime
            data['rendezvous'] = dt.strftime('%H:%M Le %m.%d.%Y')

        except Exception as identifier:
            user = None

        if user is not None and generate_token.check_token(user, token):
            user.email_confirmed = True
            user.save()

            # Get Talon
            talon, _ = Talon.objects.get_or_create(user=user)
            data['talon'] = str(talon)
            dt_c = datetime.now()
            data['create'] = dt_c.strftime('%H:%M Le %m.%d.%Y')

            pdf = async_render_to_pdf.delay('pdf/pdf_template.html', data)
            time.sleep(4)
            file_name, _status = pdf.get()
            if not _status:
                return Response({"status": 400})
            # Download Talon
            relative_path = f"pdf/{file_name}"
            absolute_path = '{}/{}.pdf'.format(settings.MEDIA_ROOT, relative_path)
            response = FileResponse(open(absolute_path, 'rb'), as_attachment=True)
            return response
        return render(request, 'auth/activate_failed.html', status=401)
