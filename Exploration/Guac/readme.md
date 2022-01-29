```sh
docker run \
	-p 8080:8080 \
	-v /guacamole:/config \
	oznu/guacamole
```

`docker run -p 8080:8080 -v /guacamole:/config oznu/guacamole`

user: guacadmin
pass: guacadmin

1. settings
2. Add user
3. Permissions
    1. Check all
4. Log back in
5. Delete default user
6. Add new connection
    1. SSH
