material_table= [
            {
                "title":"事项名称",
                "name":"item_name",
                "type":"string",
                "subtype": None,
                "required": True,
                "description":"必填，50个中文字符以内，不含空格，符号只含中英文的'()-_《》'"

            },
            {
                "title":"事项代码",
                "name":"item_code",
                "type":"string",
                "subtype": None,
                "required": True,
                "description":"必填,31个字符,只有数字或大写字母"
            },
            {
                "title":"事项内容",
                "name":"item_content",
                "type":"string",
                "subtype": None,
                "required": True,
                "description":"必填，150个中文字符以内，不含空格"
            },
            {
                "title":"政策依据",
                "name":"basis",
                "type":"string",
                "subtype": None,
                "required": True,
                "description":"政策依据（文件名，文号）,必填，100个中文字符以内，不含空格，符号只含中英文的'()-_《》'"
            },
            {
                "title":"申办所需资格条件",
                "name":"conditions",
                "type":"array",
                "subtype": "string",
                "required": True,
                "description":"必填至少一项，每项150个中文字符以内，不含空格, 增加的每一项输入不为空(只含标点符号也算空)，为空可以自动删除该项，以下数组输入同理"
            },
            {
                "title":"申办材料",
                "name":"materials",
                "type":"array",
                "subtype": "string",
                "required": True,
                "description":"必填至少一项，每项80个中文字符以内，不含空格, 增加的每一项输入不为空"
            },
            {
                "title":"法定办结时限",
                "name":"legal_limit",
                "type":"number",
                "subtype": None,
                "required": True,
                "description":"150以内的正整数，可传字符，默认60"
            },
            {
                "title":"承诺办结时限",
                "name":"promise_limit",
                "type":"number",
                "subtype": None,
                "required": True,
                "description":"150以内的正整数，可传字符，默认40"
            },
            {
                "title":"网络咨询平台", 
                "name":"consult_QR_code",
                "type":"file",
                "subtype": None,
                "required": False,
                "description":"选填，只传一张.图片，2M以内，大于0.5M适当压缩",
            },
            {
                "title":"业务办理代码", 
                "name":"service_QR_code",
                "type":"file",
                "subtype": None,
                "required": False,
                "description":"选填，只传一张.图片，2M以内，大于0.5M适当压缩",
            },
            {
                "title":"办事大厅地址",
                "name":"addresses",
                "type":"array",
                "subtype": "string",
                "required": True,
                "description":"必填至少一项，每项150个中文字符以内，不含空格, 增加的每一项输入不为空"
            },
            {
                "title":"咨询电话",
                "name":"phone_numbers",
                "type":"array",
                "subtype": "string",
                "required": True,
                "description":"必填至少一项，正则检查号码输入规范,只能为区号+8位号码，或区号+11位号码，区号请让客户单独选择，默认020, 增加的每一项输入不为空"
            }
        ]
