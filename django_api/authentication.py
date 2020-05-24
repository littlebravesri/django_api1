from rest_framework.authtoken.models import Token

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from django.utils import timezone
from django.conf import settings


def expires_in(token):
    time_elapsed = timezone.now() - token.created
    left_time = settings.TOKEN_EXPIRE_TIME - time_elapsed.seconds
    return left_time

def is_token_expired(token):
    left_time = expires_in(token)
    if left_time < 0:
        return True
    else:
        return False
    # return expires_in(token) < timedelta(seconds = 0)

def token_expire_handler(token):
    is_expired = is_token_expired(token)
    if is_expired:
        token.delete()
    elif not is_expired: # time reset
    	token.created = timezone.now() # time reset
    	token.save() # time reset
    return is_expired, token

class ExpiringTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")

        if not token.user.is_active:
            raise AuthenticationFailed("User is not active")

        is_expired, token = token_expire_handler(token)
        # print(token.created)
        if is_expired:
            raise AuthenticationFailed("The Token is expired")

        return (token.user, token)