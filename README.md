# Flask Python REST API

## Endpoints

| URL          | HTTP method | Auth | JSON Response     |
| ------------ | ----------- | ---- | ----------------- |
| /users/login | POST        |      | user's token      |
| /users       | GET         | Y    | all users         |
| /products    | GET         |      | all products      |
| /products    | POST        | Y    | new product added |
| /products    | PATCH       | Y    | edited product    |
| /products    | DELETE      | Y    | true / false      |
