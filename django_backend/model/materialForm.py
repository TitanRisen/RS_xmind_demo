import mongoengine
import datetime
from mongoengine import Document,StringField,ListField,IntField,DateTimeField

class MaterialForm(Document):
    item_code = StringField(required=True, max_length=32,unique = True)
    item_name = StringField(required=True, max_length=60)
    
    item_content = StringField(required=True, max_length=150)
    basis = StringField(required=True, max_length=100)
    conditions = ListField(StringField(max_length=150),required=True)
    materials = ListField(StringField(max_length=80), required=True)
    legal_limit = IntField(required=True)
    promise_limit = IntField(required=True)
    consult_QR_code_path = StringField(required=False, max_length=200)
    service_QR_code_path = StringField(required=False, max_length=200)
    addresses = ListField(StringField(max_length=150),required=True)
    phone_numbers = ListField(StringField(max_length=30),required=True)
    update_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        "collection": "MaterialForms",
        'index_background': True, 
        "indexes": [
            'item_code', 
            '$item_name',
            # {'fields': ('basis'), 'unique': True, 'sparse': True},    
            # {'fields': ('item_code',), 'unique': True},
            ],
    }

