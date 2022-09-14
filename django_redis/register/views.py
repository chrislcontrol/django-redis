from rest_framework.response import Response
from rest_framework.views import APIView

from django_redis.settings import redis_instance


class RegisterView(APIView):
    def post(self, request):
        key = request.data.get("key")
        value = request.data.get("value")

        redis_instance.set(key, value, ex=15)

        return Response(status=204)

    def get(self, request):
        keys = redis_instance.keys()
        return Response({key.decode('utf-8'): redis_instance.get(key) for key in keys})


class HashRegisterView(APIView):
    def post(self, request):
        key = request.data.get("key")
        value = request.data.get("value")

        redis_instance.hset(key, value)
        redis_instance.expire(key, 15)

        return Response(status=204)
