import mongoengine
import datetime
from mongoengine import Document

class Book(Document):
    author = mongoengine.StringField(required=True, max_length=125,unique = True)
    email = mongoengine.StringField(required=True)
    addr = mongoengine.StringField(required=True, max_length=125)
    time = mongoengine.DateTimeField(default=datetime.datetime.now)

# MONGO_CONN  = mongoengine.connect(
#         db="mongotest",
#         alias='default',
#         host='localhost',
#         port=27017
#         )


# book_obj = Book.objects.create(author="书民工1号", email="lowman@9527.com", addr="流浪地球村")