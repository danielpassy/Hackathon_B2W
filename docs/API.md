# Basic Usage


#### <h2>`api-token-auth`


#### `POST REQUEST - /api-token-auth`
""" <br>
Authentication method, necessary for acessing other resources on the app<br> 
"""



Field | Description
------|------------
username | The user's username 
password | The user's password
<br>
Example:

```javascript
{
  "username" : "teste",
  "password" : "teste",
}
```

Response is either a ```200 OK``` with an acess token that should be provided to other requests or  ```400 Bad Request```

```javascript
{
    "token": "65965ee99cbbb80a25961c772845d49a8713e907"
}
```

it's important to notice that the token is "token 65965ee99cbbb80a25961c772845d49a8713e907", not only the alphanumeric hash<br><br>
The following header should be included in all other requests 

        Authorization | token 65965ee99cbbb80a25961c772845d49a8713e907




#### <h2> `retrieveUserProducts`
#### `GET REQUEST - /products/user/<userID>`
""" <br>
Retrieve all products sold by an user and their details <br>
"""





an Example:
```javascript
{
}
```

Response is either a ```200 OK``` or  ```404 Not Found``` when the user is not found

```javascript
[
    {
        "categorias": [
            "Bicycle",
            "Sports"
        ],
        "name": "Road Bicycle",
        "user": 1,
        "price": 5000.36,
        "cashback": 3.0,
        "description": "Good looking bycycle",
        "active": True,
        "timestamp": "2020-08-22T22:46:22.082101Z",
        "image": "/uploads/uploads/%D7%99%D7%9C%D7%93%D7%95%D7%AA_%D7%95%D7%A0%D7%A2%D7%A8%D7%95%D7%AA.jpg"
    }, 
    {
        "categorias": [
            "shirt",
            "clothing"
        ],
        "name": "Nike Shirt",
        "user": 1,
        "price": 40.00,
        "cashback": 5.0,
        "description": "Size GG",
        "active": True,
        "timestamp": "2020-06-22T17:33:05.082101Z",
        "image": "/uploads/uploads/%D7%99%D7%9C%D7%93%D7%95%D7%AA_%D7%95%D7%A0%D7%A2%D7%A8%D7%95%D7%AA.jpg"
    } 
]
```

#### <h2> `retrieveOneProduct`
#### `GET REQUEST - /products/<str:id>`
""" <br>
Retrieve information about one specific product  
"""


an Example:
```javascript
{
}
```

Response is either a ```200 OK``` or  ```404 Not Found``` when the product is not found

```javascript
{
    "categorias": [
        "shirt",
        "clothing"
    ],
    "name": "Nike Shirt",
    "user": 1,
    "price": 40.00,
    "cashback": 5.0,
    "description": "Size GG",
    "active": True,
    "timestamp": "2020-06-22T17:33:05.082101Z",
    "image": "/uploads/uploads/%D7%99%D7%9C%D7%93%D7%95%D7%AA_%D7%95%D7%A0%D7%A2%D7%A8%D7%95%D7%AA.jpg"
} 
```

#### <h2> `createProduct`
#### `POST REQUEST - /product`
""" <br>
Create a product under the authenticated user  
"""


Field | Description
------|------------
category | Category (optional)
Price | Product price
cashback | Product cashback
description | Product description
Image | Product image (limited to 1)
 <br>
an Example:<br>

```javascript
{ 
		"product": "green jacket" 
		"category": ["coat", "clothing"] 
	    "Authorization": "token bb80a25961c772"
	    "price": 200,
	    "cashback": 10,
	    "description": "It's a really nice product, right?",
	    "image": "/uploads/uploads/img001_zyz7WaJ.jpg"
} 
```

Response is either a ```201 created```  or  ```400 bad request``` when any field is missing or improper. This should be submited from a form.

```javascript
{ 
		"product": "green jacket" 
		"category": ["coat", "clothing"] 
	    "authentication": "token bb80a25961c772"
        "user": 1,
	    "price": 200,
	    "cashback": 10,
	    "description": "It's a really nice product, right?",
	    "active": true, 
	    "timestamp": "2020-08-23T17:44:06.006233Z", 
	    "image": "/uploads/uploads/img001_zyz7WaJ.jpg"
} 
```

#### <h2> `retrieveComments`
#### `GET REQUEST - /comments/<str:id>`
""" <br>
Retrieve messages between a user and the authenticated user  
"""



an Example:
```javascript
{ 

} 
```

Response is either a ```200 OK``` or  ```404 user not found``` when any field is missing or improper. It show comments from newer to older. 

```javascript
[
    {
        "id": 6,
        "content": "It's really beatifull",
        "timestamp": "2020-08-23T20:12:34.211917Z",
        "buyer": 1,
        "seller": 2
    },
    {
        "id": 5,
        "content": "I was really thinking about buying this jacket",
        "timestamp": "2020-08-23T20:12:26.348271Z",
        "buyer": 1,
        "seller": 2
    }
]
```

#### <h2> `createComment`
#### `GET REQUEST - /comment`
""" <br>
Create a message from the authenticated user to a specific user
"""


an Example:
```javascript
{ 

} 
```

Responsse is a ```200 OK```

```javascript
{
    "id": 9,
    "content": "Hello, I'm interested on this cellphone",
    "timestamp": "2020-08-24T01:33:53.665446Z",
    "buyer": 3,
    "seller": 2
}
```
#### <h2> `retrieveTransactions`
#### `GET REQUEST - /transactions/list`
""" <br>
Retrieve the Authenticated User transactions  
"""


Field | Description
------|------------
product | product id
<br>

an Example:
```javascript
{ 
    "product":1
} 
```

Response is a ```200 OK```

```javascript
[
    {
        "id": 4,
        "price": 1000.0,
        "cashback": 50.0,
        "timestamp": "2020-08-23T21:33:28.329430Z",
        "product": 10,
        "seller": 1,
        "buyer": 2
    },
    {
        "id": 3,
        "price": 1000.0,
        "cashback": 100.0,
        "timestamp": "2020-08-23T21:06:32.891238Z",
        "product": 1,
        "seller": 1,
        "buyer": 2
    }
]
```
#### <h2> `createTransaction`
#### `POST REQUEST - /transaction`
""" <br>

Create a transaction representing the buying of a product<br>
"""


an Example:
```javascript
{ 
    "product": 3
} 
```

Response is either a ```201 created```  or  ```403 Forbidden``` when the object is no more available. This should be submited from a form.

```javascript
{
    "id": 5,
    "price": 5000.36,
    "cashback": 75.0,
    "timestamp": "2020-08-24T01:46:54.684233Z",
    "product": 5,
    "seller": 1,
    "buyer": 2
}
```