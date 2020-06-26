import mongoengine
from materialForm import MaterialForm



form = {
    'item_name': "???????", 
    'item_code':"123456", 
    'item_content':"????????",
    'basis':"test_123",
    'conditions':[
        '????1',
        '????2'
    ],
    'materials':[
        '????1',
        '????2'
    ],
    'legal_limit':10,
    'promise_limit':20,
    # 'consult_QR_code_path':'/user',
    # 'service_QR_code_path':'/user',
    'addresses':[
        '???1'
    ],
    'phone_numbers':[
        '12345678',
    ]



} 

# if "__name__" == "__main__":
MONGO_CONN  = mongoengine.connect(
        db="mongotest",
        alias='default',
        host='localhost',
        port=27017
        )

obj = MaterialForm.objects.create(**form)
