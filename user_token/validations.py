from user_token import models


class TokenValidation:
    def check_token(value):
        return bool(models.UserToken.objects.filter(token=value))
