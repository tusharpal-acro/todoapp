# TodoApp
A django REST API app for creating TODO list with Nested Categories

## Models

1. Category
2. Todo

## To Run the project and access the API

Direct to the project folder directory

Create a virtual environment for python3 using:

```python3 -m venv environment_name```

Activating a virtual environment:

```source environment_name/bin/activate```

### If you want to run through Docker, follow below steps:

Below two command will install all the requirements by building the container and run the server:

To build docker compose file in order to create container of required images (make sure you are in directory where docker-compose file exist).

```bash
docker-compose build
```
To setup (activate) the container
```bash
docker-compose up
```

Check server running at http://localhost:8000/ 
This must be printing: "Todo API App  with Nested Categories"

To manage admin interface, we need to open another terminal and use the below mentioned command,
```bash
docker exec -it {container_id} python manage.py createsuperuser
```

### If you do not want to run through Docker, run the below three commands:
Installing all libraries in requirements file inside the virtual environment:

```pip3 install -r requirements.txt```

To set-up the database:

```python3 manage.py makemigrations```

```python3 manage.py migrate```

Running the project on the localhost:

```python3 manage.py runserver```

Check for running server:

http://localhost:8000/

This must be printing: "Todo API App  with Nested Categories"

To manage admin interface, we need to create a super user.
To create a super user, execute the below command:

````docker exec -it {container_id} python manage.py createsuperuser````


The server is running now. Head on to the below API endpoints:

## CRUD APIs for Category

### Create

```/create-category/```

params:
```json
{
    "name": ""
}
```
###List Categories

```/categories/```

### Retrieve

```/retrieve-category/id/```

### Update

```/update-category/id/```

### Delete

```/delete-category/id/```

### Fetch task in Category

```/taskbycategory/{category-name}/```



## CRUD APIs for Tasks (Todo model)

### Create

```/create-todo/```

params:
```json
{
    "name": "",
    "description": "",
    "category": "",
    "date_assigned": ""
}
```
###List Todo

```/todos/```

### Retrieve

```/retrieve-todo/{{id}}/```

### Update

```/update-todo/{{id}}/```

### Delete

```/delete-todo/{{id}}/```

## Caching 

File Based Caching enabled for 60 seconds

## Testing

Test using:

````python3 manage.py test````
