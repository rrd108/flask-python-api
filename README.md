# Flask Python REST API

## Video
[Python REST API építés 50 perc alatt Flask-kel](https://www.youtube.com/watch?v=qNjVCqU-Xcg)

## Endpoints

| URL          | HTTP method | Auth | JSON Response     |
| ------------ | ----------- | ---- | ----------------- |
| /users/login | POST        |      | user's token      |
| /users       | GET         | Y    | all users         |
| /products    | GET         |      | all products      |
| /products    | POST        | Y    | new product added |
| /products    | PATCH       | Y    | edited product    |
| /products    | DELETE      | Y    | true / false      |
