![titulo](/docs/titulo.JPG)

# Python-Flask

Creating a web API with Python and Flask.

## Objective

In this project you will learn how to create a web API in Python, make requests and connect it with a local and a remote database.

## Technologies

- [VSCode](https://code.visualstudio.com/)
- [Python](https://www.python.org/)
- [Flask](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#lesson-goals)
- [PyMySQL](https://pymysql.readthedocs.io/en/latest/index.html)

## Before Start

If you are new to Python, read these articles to get started: [Python for Beginners](https://dev.to/lucianopereira86/python-for-beginners-part-1-hello-world-19ed).

## Topics

- [venv](#venv)
- [API](#api)
- [GET](#get)
- [POST](#post)
- [PUT](#put)
- [DELETE](#delete)
- [Local Database](#local-database)
- [Remote Database](#remote-database)

### venv

Create a folder for your project, open VSCode and execute the command below to create a virtual environment (venv):

```sh
python -m venv venv
```

Confirm any popup that shows up and run the command below to use the _venv_:

```sh
.\venv\Scripts\Activate.ps1
```

Create a file named 'requirements.txt' containing the word _flask_.

![venv01](/docs/venv01.JPG)

Install the _flask_ package inside the _venv_ with the following command:

```sh
pip install -r requirements.txt
```

The result will be:

![venv02](/docs/venv02.JPG)

### API

Create a folder called _api_ with a file called _api.py_. Inside the file, write this code:

![flask01](/docs/flask01.JPG)

Run the following command:

```sh
python .\api\api.py

```

The result will be:
![flask02](/docs/flask02.JPG)

If you follow the URL displayed you will see the web page running:

```
http://127.0.0.1:5000/
```

![flask03](/docs/flask03.JPG)

### GET

Now, let's change our route to be used as a regular web API.  
Create a dictionary called _users_dict_ to be returned after a GET request:

![flask04](/docs/flask04.JPG)

Access the URL below and see the result:

```
http://127.0.0.1:5000/users
```

![flask05](/docs/flask05.JPG)

Let's create another method to return a user by id:

![flask06](/docs/flask06.JPG)

Access the URL below and see the result:

```
http://127.0.0.1:5000/user?id=1
```

![flask07](/docs/flask07.JPG)

Return a user by id passing the parameter in the path:

![flask08](/docs/flask08.JPG)

Access the URL below and see the result:

```
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

We have added a new user to the _users_dict_. Let's make some changes at the _get_users_ function to search for the user by using multiple properties dynamically, even by considering their types.

| Don't forget to run the POST request every time you save the project because the _users_dict_ will be resetted! |
| --------------------------------------------------------------------------------------------------------------- |


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

### Local Database

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

```sh
python .\api\db_api.py

```

The _test.db_ will be created inside the _api_ folder and will contain the _user_ table:

![flask28](/docs/flask28.JPG)

Copy and modify the HTTP functions from _api.py_ to _db_api.py_.

- POST

![flask29](/docs/flask29.JPG)

- PUT

![flask30](/docs/flask30.JPG)

- GET

![flask31](/docs/flask31.JPG)

- DELETE

![flask32](/docs/flask32.JPG)

Test each one and see the result.

### Remote Database

Let's connect with a remote MySQL database now.  
Follow the instructions in this [article](https://dev.to/lucianopereira86/net-core-web-api-part-2-mysql-3bje) or in this [repository](https://github.com/lucianopereira86/NetCore3-MySQL) to create a database and get the connection string.  
If you followed them correctly, you must have a _user_ table in your remote database. Change it by adding a column named _age_.  
Here is an easy script to do it:

```sql
ALTER TABLE user ADD age INT NOT NULL;
```

Now, return to VSCode, add _PyMySQL_ into the _requirements.txt_ and install it by running:

```sh
pip install -r requirements.txt
```

Inside the _db_api.py_, import the _PyMySQL_ package:

```python
import pymysql.cursors
```

Comment the _start_db_ function because it won't be needed anymore:

![flask33](/docs/flask33.JPG)

Modify the _execute_ function to receive the MySQL connection by adding the connection string:

![flask34](/docs/flask34.JPG)

Change the _post_users_ function to receive the inserted id:

![flask35](/docs/flask35.JPG)

Now, run the API again:

```sh
python .\api\db_api.py

```

Make a GET request to the _get_users_ function. The result will be something like this:

![flask38](/docs/flask38.JPG)

Make a POST request to create another user:

![flask39](/docs/flask39.JPG)

Another GET request and the result will be:

![flask40](/docs/flask40.JPG)

Modify the age from your new user with a PUT request:

![flask41](/docs/flask41.JPG)

Check it out:

![flask42](/docs/flask42.JPG)

Delete another user:

![flask43](/docs/flask43.JPG)

And... it is gone!

![flask44](/docs/flask44.JPG)

## Conclusion

In this great project we have seen how a web API behaves in a Python environment with Flask framework.  
During our tests, we have used runtime variables (_api.py_) and persistent data (_db_api.py_).  
The local and remote database had similar functions, equal results and were easy to manipulate.
