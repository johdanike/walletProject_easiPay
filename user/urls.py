from djoser.serializers import UserCreateSerilizer as BaseUserCreateSerilizer


class UserCreateSerilizer(BaseUserCreateSerilizer):
    class Meta(BaseUserCreateSerilizer.Meta):
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'phone_number')