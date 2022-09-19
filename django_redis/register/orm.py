import uuid

from redis import Redis

from django_redis.settings import REGISTER_COLLECTION


class RedisHandler:
    def __init__(self, host="localhost", port=6379):
        self.host = host
        self.port = port
        self.session = None

    def __enter__(self, *args, **kwargs):
        self.session = Redis(host=self.host, port=self.port, db=0, decode_responses=True)
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


class RegisterRepository:
    collection = REGISTER_COLLECTION

    def create_register(self, value: dict):
        key = str(uuid.uuid4())

        with RedisHandler() as redis:
            collection = f"{self.collection}:{key}"

            redis.hset(name=collection, key="id", value=key, mapping=value)
            redis.expire(collection, 5)

        return value

    def list_all(self):
        with RedisHandler() as redis:
            keys = self.get_keys()
            registers = [redis.hgetall(key) for key in keys]

        return registers

    def get_by_collection_and_id(self, id: str):
        with RedisHandler() as redis:
            registers = redis.hgetall(name=f"{self.collection}:{id}")

        return registers

    def get_keys(self):
        with RedisHandler() as redis:
            keys = redis.keys(f"{self.collection}:*")
        return keys
