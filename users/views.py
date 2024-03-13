from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from users.models import User
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
# Create your views here.


class UserView(views.APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    def get(self,request):
        id = request.query_params.get('id')
        instance = User.objects.get(id=id)
        data = UserSerializer(instance=instance).data
        return Response(data=data,status=status.HTTP_200_OK)