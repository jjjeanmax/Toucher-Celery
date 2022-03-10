from django.contrib.auth.tokens import PasswordResetTokenGenerator

import six

from RendezVous.settings.secret import get_secret


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.email_confirmed))


generate_token = TokenGenerator()


data = {
    "company": get_secret(section='DATA', setting='company'),
    "address": get_secret(section='DATA', setting='address'),
    "city": get_secret(section='DATA', setting='city'),
    "state": get_secret(section='DATA', setting='state'),
    "zipcode": get_secret(section='DATA', setting='zipcode'),
    "phone": get_secret(section='DATA', setting='phone'),
    "email": get_secret(section='DATA', setting='email'),
    "website": get_secret(section='DATA', setting='website'),
}
