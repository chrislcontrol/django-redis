from rest_framework.response import Response
from rest_framework.views import APIView

from django_redis.register.orm import RegisterRepository, RedisHandler


class RegisterView(APIView):
    def post(self, request):
        key = request.data.get("key")
        value = request.data.get("value")
        with RedisHandler().session() as redis:
            redis.set(key, value, ex=15)

        return Response(status=204)

    def get(self, request):
        repo = RegisterRepository()
        registers = repo.list_all()

        return Response(data=registers, status=200)


class HashRegisterView(APIView):
    def post(self, request):
        repo = RegisterRepository()

        register = repo.create_register(request.data)

        return Response(data=register, status=201)


class HashRegisterDetailView(APIView):
    def get(self, request, id):
        repo = RegisterRepository()

        register = repo.get_by_collection_and_id(id)

        return Response(data=register, status=200)
