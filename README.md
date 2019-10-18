![titulo](/docs/titulo.JPG)

# Python-Flask

Creating a web API with Python and Flask.

## References

This [article](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#lesson-goals) from the Programming Historian website explains very well how to use Python with Flask and is being used as reference for this project.

## Topics

- [venv](#venv)
- [API](#api)
- [GET](#get)
- [POST](#post)
- [PUT](#put)
- [DELETE](#delete)
- [Database Connection](#database-connection)
- [Database Operations](#database-operations)

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
Create a dictionary called \_users_dict to be returned after a GET request:

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
Create another Python file inside the _api_ folder called _db_api_ and write the functions below:

- Creates the database

![flask24](/docs/flask24.JPG)

- Creates tables

![flask25](/docs/flask25.JPG)

- Starts the database. Must be called before _app.run()_.

![flask26](/docs/flask26.JPG)

- Dictionary factory and cursor

![flask27](/docs/flask27.JPG)

Finally, run the following command:

```bash
python .\api\db_api.py

```

The _test.db_ is created inside the _api_ folder and contains the _user_ table:

![flask28](/docs/flask28.JPG)

### Database Operations

- POST

![flask29](/docs/flask29.JPG)

- GET

![flask30](/docs/flask30.JPG)

- PUT

![flask31](/docs/flask31.JPG)

- DELETE

![flask32](/docs/flask32.JPG)
