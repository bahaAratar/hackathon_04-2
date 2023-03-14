from rest_framework import serializers
from django.contrib.auth import get_user_model
from .tasks import send_activation_code, send_reset_password_code

User = get_user_model()

class RegisterFreelancerSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        min_length=6,
        error_messages={
            'min_length': 'Password must be at least 6 characters long.',
            'required': 'Password confirmation is required.'
        }
    )

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'experience', 'education', 'rating', 'email', 'password', 'password2')

    def validate_email(self, email):
        return email
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')

        if password != password2:
            raise serializers.ValidationError({'password2': 'Passwords do not match.'})

        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code.delay(user.email, user.activation_code)
        return user

class RegisterClientSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        min_length=6,
        error_messages={
            'min_length': 'Password must be at least 6 characters long.',
            'required': 'Password confirmation is required.'
        }
    )

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'rating', 'email', 'password', 'password2')

    def validate_email(self, email):
        return email
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.pop('password2')

        if password != password2:
            raise serializers.ValidationError({'password2': 'Passwords do not match.'})

        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code.delay(user.email, user.activation_code)
        return user
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User with this email does not exist.')
        return email
    
    def send_reset_password_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()
        send_reset_password_code.delay(email=email, code=user.activation_code)

class ForgotPasswordComleteSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, min_length=6)
    password_confirm = serializers.CharField(required=True, min_length=6)
    code = serializers.CharField(required=True)

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')

        if password != password_confirm:
            raise serializers.ValidationError({'password_confirm': 'Passwords do not match.'})

        return attrs
    
    def validate_code(self, code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Invalid code.')
        return code
    
    def set_new_password(self):
        user = User.objects.get(activation_code=self.validated_data.get('code'))
        password = self.validated_data.get('password')
        user.set_password(password)
        user.activation_code = ''
        user.save(update_fields=['password', 'activation_code'])
