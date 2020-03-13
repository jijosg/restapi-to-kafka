# restapi-to-kafka
Post to Kafka topic from an api built on Flask

## Install flask
---
```
pip install flask
```

## Set environment variables
---
```
set FLASK_APP=flaskr 
set FLASK_ENV=development
```
## Run flask
---
```
flask run
```

## Post using POSTMAN
----
Postman has some built in variables that gives us random values which can be used to 
construct/mock a json input


```
POST: localhost:5000/posttokafka
Body : 
{
    "streetName" : "{{$randomStreetName}}",
    "country" : "{{$randomCountry}}",
    "phrase" : "{{$randomCatchPhrase}}"
}
```