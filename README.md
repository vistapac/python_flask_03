# python_flask_03

[測試站](http://127.0.0.1:5000/) - /python_flask_03/python_flask_03/

##### 用戶登入與簡單權限控制 API
* 版本 - 3.0

Base URLs:

# Default

## POST 註冊

POST /api/register

> Body 请求参数

```json
{
  "email": "string",
  "password": "string",
  "username": "string",
  "role": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» email|body|string| 是 | 信箱|none|
|» password|body|string| 是 | 密碼|none|
|» username|body|string| 否 | 名稱|none|
|» role|body|string| 否 | 權限|user/admin|

> 返回示例

> 200 Response

```json
{
  "message": "string",
  "data": {
    "email": "string",
    "username": "string",
    "role": "string",
    "id": "string"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» message|string|true|none|訊息|none|
|» data|object|true|none||none|
|»» email|string|true|none|註冊信箱|none|
|»» username|string|true|none|用戶名|none|
|»» role|string|true|none|權限|none|
|»» id|string|true|none|id|none|

## POST 登入

POST /api/login

> Body 请求参数

```json
{
  "email": "string",
  "password": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|body|body|object| 否 ||none|
|» email|body|string| 是 ||none|
|» password|body|string| 是 ||none|

> 返回示例

> 200 Response

```json
{
  "message": "string",
  "data": {
    "id": "string",
    "email": "string",
    "username": "string",
    "role": "string",
    "token": "string"
  }
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» message|string|true|none|訊息|none|
|» data|object|true|none||none|
|»» id|string|true|none|id|none|
|»» email|string|true|none|註冊信箱|none|
|»» username|string|true|none|用戶名|none|
|»» role|string|true|none|權限|none|
|»» token|string|true|none|jwt|none|

## GET 取得

GET /api/user

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|Authorization|header|string| 是 ||Bearer <JWT token>|

> 返回示例

> 200 Response

```json
{
  "id": "string",
  "email": "string",
  "username": "string",
  "role": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» id|string|true|none|id|none|
|» email|string|true|none|註冊信箱|none|
|» username|string|true|none|用戶名|none|
|» role|string|true|none|權限|none|

## PUT 修改

PUT /api//users/{user_id}/role

> Body 请求参数

```json
{
  "role": "string"
}
```

### 请求参数

|名称|位置|类型|必选|中文名|说明|
|---|---|---|---|---|---|
|user_id|path|string| 是 ||none|
|Authorization|header|string| 否 ||Bearer <JWT token>|
|body|body|object| 否 ||none|
|» role|body|string| 是 | 權限|none|

> 返回示例

> 200 Response

```json
{
  "message": "string"
}
```

### 返回结果

|状态码|状态码含义|说明|数据模型|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|成功|Inline|

### 返回数据结构

状态码 **200**

|名称|类型|必选|约束|中文名|说明|
|---|---|---|---|---|---|
|» message|string|true|none|訊息|none|

# 数据模型



#####   備忘錄
requirements.txt
├── Flask               v3.0.3
├── Flask-SQLAlchemy    v3.1.1
├── flask_jwt_extended  v4.6.0
├── werkzeug            v3.0.0
├── PyMySQL             v1.1.1
├── python-dotenv       v1.0.1
├── pytest              v8.2.2
└── pytest-flask        v1.3.0

#####   安裝
pip install -r requirements.txt

#####   執行
python app.py

#####   測試
pytest