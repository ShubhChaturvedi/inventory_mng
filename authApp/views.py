from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        return Response(users.values())
