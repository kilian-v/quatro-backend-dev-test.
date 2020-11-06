from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .renderers import UserJSONRenderer
from .serializer import RegistrationSerializer, LoginSerializer
from rest_framework_api_key.models import APIKey


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        public_key = APIKey.objects.create_key(name="public-key" + "-" + request.data.get("username"))
        private_key = APIKey.objects.create_key(name="private-key" + "-" + request.data.get("username"))
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ApiKeyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.user.username
        public_key = APIKey.objects.get(name="public-key" + "-" + username)
        private_key = APIKey.objects.get(name="private-key" + "-" + username)

        return Response({
            public_key.name: public_key.id,

            private_key.name: private_key.id,
        })


class RestaurantsView(APIView):

    def post(self, request):
        username = request.user.username
        public = APIKey.objects.get(name="public-key" + "-" + username)
        private = APIKey.objects.get(name="private-key" + "-" + username)
        public_key = request.META["HTTP_X_PUBLIC_KEY"]
        private_key = request.META["HTTP_X_PRIVATE_KEY"]
        if public_key != public.id:
            return Response("Please enter a valid Public Key")
        if private_key != private.id:
            return Response("Please enter a valid Private Key")
        data = request.data
        location = (data['lat'], data['lng'])
        return Response("List of Restaurants")
