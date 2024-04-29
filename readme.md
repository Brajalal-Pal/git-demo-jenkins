# Python Installation steps:

## Create a virtual environment
$ python -m venv env

## Activate the virtual environment
$ source env/Script/activate

## Install the required packages
$ pip install -r requirements.txt

## Run the application
$ python app.py

## Check which version of pip is installed on your system
$ python -m pip --version

## Check which library installed on our sytem?
$ pip list


## Tutorial Link 
[F:\Tutorials\Python Programming\FastAPI\Udemy - FastAPI - The Complete Course 2023 (Beginner + Advanced)]

# FastAPI Project setup
$ pip install fastapi
$ pip install uvicorn


Default library installs on installing fastapi & uvicorn are:
-----------------------------------------------------------
$ pip list
Package           Version
----------------- -------
annotated-types   0.6.0
anyio             4.3.0
click             8.1.7
colorama          0.4.6
fastapi           0.110.0
h11               0.14.0
idna              3.6
pip               24.0
pydantic          2.6.3
pydantic_core     2.16.3
sniffio           1.3.1
starlette         0.36.3
typing_extensions 4.10.0
uvicorn           0.28.0


## SQLite commands:

$ sqlite3 todos.db
SQLite version 3.42.0 2023-05-16 12:36:15
Enter ".help" for usage hints.
sqlite> .schema
CREATE TABLE todos (
        id INTEGER NOT NULL,
        title VARCHAR,
        description VARCHAR,
        priority INTEGER,
        complete BOOLEAN,
        PRIMARY KEY (id)
);
CREATE INDEX ix_todos_id ON todos (id);

sqlite> insert into todos(title, description, priority, complete) values('Go to the store','Pick up eggs',5,False);

sqlite> insert into todos(title, description, priority, complete) values('Cut the lawn','Grass is getting long',3,False); 

sqlite> insert into todos(title, description, priority, complete) values('Feed the dog','He is getting hungry',5,False); 


sqlite> .mode markdown
sqlite> select * from todos;
| id |      title      |      description      | priority | complete |
|----|-----------------|-----------------------|----------|----------|
| 1  | Go to the store | Pick up eggs          | 5        | 0        |
| 2  | Cut the lawn    | Grass is getting long | 3        | 0        |
| 3  | Feed the dog    | He is getting hungry  | 5        | 0        |

## other modes are:
sqlite> .mode box

sqlite> .mode column

sqlite> .mode table
