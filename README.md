### Put 10 messages into database

```sh
$ for i in {1..10}; do curl http://localhost:9150 -X POST --data "msg=msg$i"; done
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
```

![[1.png]]

### Get that messages

```shell
$ curl http://localhost:9150 
msg3, msg5, msg1, msg6, msg4, msg7, msg2, msg10, msg9, msg8 : This service hasn't been implemented yet%
```

![[2.png]]

### Turn off service on 11004 and 11005 ports

```
$ curl http://localhost:9150 
msg3, msg5, msg1, msg6, msg4, msg7, msg2, msg10, msg9, msg8 : This service hasn't been implemented yet%

$ curl http://localhost:9150 
msg3, msg5, msg1, msg6, msg4, msg7, msg2, msg10, msg9, msg8 : This service hasn't been implemented yet%
```

There was few unsuccessful requests in curl because randomly selected services had been stopped.

![[3.png]]


