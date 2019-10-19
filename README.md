![titulo](/docs/titulo.JPG)

# Python-Flask

Creating a web API with Python and Flask.

## Objective

In this project you will learn how to create a web API in Python, connect it with a database, make requests and integrate it with Swagger for a better interaction.

## Technologies

- Python
- Flask
- Flasgger

## Topics

- [venv](#venv)
- [API](#api)
- [GET](#get)
- [POST](#post)
- [PUT](#put)
- [DELETE](#delete)
- [Database Connection](#database-connection)
- [Database Operations](#database-operations)
- [Swagger](#swagger)

### venv

Execute the command below to create a virtual environment (venv):

```bash
python -m venv venv
```

Confirm any popup that shows up and run the command below to use the _venv_:

```bash
.\venv\Scripts\Activate.ps1
```

Create a file named 'requirements.txt' containing the word _flask_.

![venv01](/docs/venv01.JPG)

Install the _flask_ package inside the _venv_ with the following command:

```bash
pip install -r requirements.txt
```

The result will be:

![venv02](/docs/venv02.JPG)

### API

Create a folder called _api_ with a file called _api.py_. Inside the file, write this code:

![flask01](/docs/flask01.JPG)

Run the following command:

```bash
python .\api\api.py

```

The result will be:
![flask02](/docs/flask02.JPG)

If you follow the URL displayed you will see the web page running:

```bash
http://127.0.0.1:5000/
```

![flask03](/docs/flask03.JPG)

### GET

Now, let's change our route to be used as a regular web API.  
Create a dictionary called _users_dict_ to be returned after a GET request:

![flask04](/docs/flask04.JPG)

Access the URL below and see the result:

```bash
http://127.0.0.1:5000/users
```

![flask05](/docs/flask05.JPG)

Let's create another method to return a user by id:

![flask06](/docs/flask06.JPG)

Access the URL below and see the result:

```bash
http://127.0.0.1:5000/user?id=1
```

![flask07](/docs/flask07.JPG)

Return a user by id passing the parameter in the path:

![flask08](/docs/flask08.JPG)

Access the URL below and see the result:

```bash
http://127.0.0.1:5000/user/1
```

![flask09](/docs/flask09.JPG)

### POST

To simulate a POST request, let's remove all dictionaries from _users_dict_:

![flask10](/docs/flask10.JPG)

Create a POST method with the following code:

![flask11](/docs/flask11.JPG)

Execute a POST request sending a new user. I've chosen [Postman](https://www.getpostman.com/) to make the request:

![flask12](/docs/flask12.JPG)

The result will be:

![flask13](/docs/flask13.JPG)

We have added a new user to the _user_dict_. Let's make some changes at the _get_users_ function to search for the user by using multiple properties dynamically, even considering their types.

![flask14](/docs/flask14.JPG)

This way we have many possible queries with the same method:

![flask15](/docs/flask15.JPG)

![flask16](/docs/flask16.JPG)

![flask17](/docs/flask17.JPG)

### PUT

To update a user, create this method:

![flask18](/docs/flask18.JPG)

Execute a PUT request:

![flask19](/docs/flask19.JPG)

Run another query to see the result:

![flask20](/docs/flask20.JPG)

### DELETE

To delete a user by id, write this code:

![flask21](/docs/flask21.JPG)

Execute a DELETE request:

![flask22](/docs/flask22.JPG)

Run another query to see the result:

![flask23](/docs/flask23.JPG)

## Database Connection

It's time to finally connect with a database to persist the data.  
Create another Python file inside the _api_ folder called _db_api_ and write this code:

![flask24_0](/docs/flask24_0.JPG)

The functions below must be created as well:

- Creates the database

![flask24](/docs/flask24.JPG)

- Creates tables

![flask25](/docs/flask25.JPG)

- Executes the operation

![flask27](/docs/flask27.JPG)

- Starts the database. This function must be called before _app.run()_.

![flask26](/docs/flask26.JPG)

Finally, run the following command:

```bash
python .\api\db_api.py

```

The _test.db_ will be created inside the _api_ folder and will contain the _user_ table:

![flask28](/docs/flask28.JPG)

### Database Operations

Copy and modify the HTTP functions from _api.py_ to _db_api.py_.

- POST

![flask29](/docs/flask29.JPG)

- PUT

![flask30](/docs/flask30.JPG)

- GET

![flask31](/docs/flask31.JPG)

- DELETE

![flask32](/docs/flask32.JPG)

### Swagger

Instead of using a web browser and Postman, let's improve our interaction with the web API by using Swagger, a web page that allows user interaction and documentation. First, follow these steps:

- Delete the _venv_ folder.
- Reopen the VSCode.
- Edit the _requirements.txt_ by adding a line with _flasgger_.
- Recreate the [venv](#venv).

Inside the _api_ folder, create a folder named _yml_ containing the _get.yml_ file:

![flask33](/docs/flask33.JPG)

The following code presents the input parameters and the expected output from the GET method.  
Put it inside the _get.yml_.

```batch
List all users
Send the parameters _id_, _age_ and _name_.
---
tags:
  - List Users
parameters:
  - name: id
    in: query
    type: integer
    description: the user id
  - name: age
    in: query
    type: integer
    description: the user age
  - name: name
    in: query
    type: string
    description: the username
responses:
  500:
    description: Internal Server Error
  200:
    description: Success
    schema:
      type: array
      items:
        id: user
        properties:
          id:
          type: integer
            description: the user id
            default: 1
          age:
            type: integer
            description: the user id
            default: 33
          name:
            type: string
            description: the user name
            default: Luciano

```

Import _flasgger_ inside of _db_api.py_:

```bash
from flasgger import Swagger
from flasgger.utils import swag_from
```

Change the GET method to receive the Swagger documentation by adding the _swag_from_ decorator:

![flask34](/docs/flask34.JPG)

Run the API and access this URL:

```batch
http://localhost:5000/apidocs/index.html
```

The _flagger_ page will be accessible:

![flask35](/docs/flask35.JPG)

## References

Flask: [https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#lesson-goal](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#lesson-goals).

Flasgger: [http://brunorocha.org/python/flask/flasgger-api-playground-with-flask-and-swagger-ui.html](http://brunorocha.org/python/flask/flasgger-api-playground-with-flask-and-swagger-ui.html).
