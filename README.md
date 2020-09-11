# Inistock Portfolio management platform - REST API

This is a Portfolio management API that allows you to create your profile and add all your investments
together in one place.

## Install
Clone the project and start building a development environment

 1. Install the dependencies of project
 ```
 $ pip install -r requirements.txt
 ```
 
 2. Create the .env file and add the variables
 ```
 POSTGRES_DB_NAME=''
 POSTGRES_DB_USERNAME=''
 POSTGRES_DB_PASSWORD=''
 POSTGRES_HOST=''
 POSTGRES_PORT=''
 ```
 
## Run the app

```
 $ python manage.py runserver
```

## REST API - ENDPOINT STRUCTURE
| Endpoint | Method | Description |
| --------|:---------:|:----------|
| /v1/person | POST | Create a new person |
| /v1/person/<person_id> | GET | Retrieve a person based on id |
| /v1/person/<person_id> | PATCH | Update a person |
| /v1/share | GET| Retrieve a list of shares |
| /v1/share/<share_id>| GET | Retrieve a share |
| /v1/share/<share_id> | DELETE | Delete a share |
| /v1/share/<share_id> | PATCH | Update a share |

## Errors
The Inistock API uses conventional HTTP response codes to indicate errors, and includes more detailed information on the exact
nature of an error in the HTTP response.

<hr/>


#### HTTP RESPONSE CODES

| RESPONSE CODE | MESSAGE    |
| ------------- |:----------:|
| 200 OK        | All is well|
| 201 CREATED   | A resource has been created |
| 400 BAD REQUEST | Your request has missing arguments |
| 405 METHOD NOT ALLOWED | You are using an incorrect HTTP verb |
| 404 NOT FOUND | The endpoint requested does not exist |
| 500 INTERNAL SERVER ERROR | Something is wrong on our end |

## License & Author
License 2020 © MIHAIL BUTNARU

Made by Mihail Butnaru
