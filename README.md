# rest-minimal

A miminmal REST api for testing GET/POST during developement.


## Available routes

```http://localhost:5000/```

- supports POST & GET methods
- returns 200 and request json or "hello world" for empty requests



```http://localhost:5000/send_email/```

- supports POST & GET methods
- returns 200 and request json or "hello world" for empty requests
- sends an email


## docker

Create a .env file with necessary variable (refer to docker-compose.yaml)

```
docker-compose build
```

```
docker-compose up
```


## helm install

```
helm3 install rest-minimal helm/rest-minimal/ --values ~/helm/rest-minimal/values.yaml
```

## helm upgrade

```
helm3 upgrade rest-minimal helm/rest-minimal/ --values ~/helm/rest-minimal/values.yaml
```
