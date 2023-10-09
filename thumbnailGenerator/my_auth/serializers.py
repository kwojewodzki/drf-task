from django.contrib.auth import authenticate

from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label='Password',
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(requests=self.context.get('request'), username=username, password=password)

            if not user:
                raise serializers.ValidationError('Wrong credentials were provided', code='authorization')
        else:
            raise serializers.ValidationError('Both fields are required', code='authorization')

        attrs['user'] = user
        return attrs
