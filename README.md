# restapi-to-kafka
Post data to Kafka topic from an simple api built on Flask, and read it using a Consumer built on scala.

## Install flask
```
pip install flask
```

## Set environment variables
```
set FLASK_APP=restapi-to-kafka 
set FLASK_ENV=development
```
## Run flask
```
flask run
```

## Post using POSTMAN
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

## Use kafka-consumer sbt project to consume data from the kafka topic
Compile the project using sbt and run `Consumer.scala`
