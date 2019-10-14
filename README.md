![titulo](/docs/titulo.JPG)

# Python-Flask

Creating a web API with Python and Flask.

## References

This [article](https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask#lesson-goals) from the Programming Historian website explains very well how to use Python with Flask and is being used as reference for this project.

## Topics

- [venv](#venv)
- [Flask](#flask)

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

## Flask

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

Now, let's change our route to be used as a common web API.
Create a dictionary called _users_ and return it when happens a GET method request:

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
