### Sending POST request to facade  service 11 times, and then GET request to get all the messages:
```sh
$ for i in {10..20}; do curl http://localhost:9150 -X POST --data "msg=$i"; done
200
200
200
200
200
200
200
200
200
200
200

$ curl http://localhost:9150       
10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 : This service hasn't been implemented yet%                             
```

### Facade service 
```sh
$ flask --app=facade_service run --port 9150
 * Serving Flask app 'facade_service'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:9150
Press CTRL+C to quit
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST / HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2023 23:37:25] "GET / HTTP/1.1" 200 -

```

### Logging service

```sh
$ flask --app=logging_service run --port 9151
 * Serving Flask app 'logging_service'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:9151
Press CTRL+C to quit
fc72beeb-f790-36ee-a73d-33888c9d8880 	 10
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST /log HTTP/1.1" 200 -
1e46afa2-6176-3cd3-9750-3015846723df 	 11
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST /log HTTP/1.1" 200 -
0042b01d-95bd-343f-bd9f-3186bfd63508 	 12
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST /log HTTP/1.1" 200 -
115ff52f-d605-3b4b-98fe-c0ea57f4930c 	 13
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST /log HTTP/1.1" 200 -
ed0221e8-ac7d-393b-821d-25183567885b 	 14
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST /log HTTP/1.1" 200 -
508ef333-85a6-314c-bcf3-17ddc32b2216 	 15
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST /log HTTP/1.1" 200 -
a4715ee0-524a-37cc-beb2-a0b5030757b7 	 16
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST /log HTTP/1.1" 200 -
d1c72756-aaec-3470-a2f2-97415f44d72f 	 17
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST /log HTTP/1.1" 200 -
7aec2f01-586e-3d53-b8f3-6cf7e6b649a4 	 18
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST /log HTTP/1.1" 200 -
3d234b88-8d6f-319a-91ea-edb6059fc825 	 19
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST /log HTTP/1.1" 200 -
d2568554-93ec-30c7-9e15-f383be19e5bb 	 20
127.0.0.1 - - [28/Apr/2023 23:37:00] "POST /log HTTP/1.1" 200 -
127.0.0.1 - - [28/Apr/2023 23:37:25] "GET /log HTTP/1.1" 200 -

```


### Messages service
```sh
$ flask --app=messages_service run --port 9152
 * Serving Flask app 'messages_service'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:9152
Press CTRL+C to quit
127.0.0.1 - - [28/Apr/2023 23:37:25] "GET /message HTTP/1.1" 200 -

```