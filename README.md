## Prerequisites
> 👉 You should have Docker installed on your local machine [link](https://www.docker.com)

## Installing instructions
> 👉 Clone this repository  

```bash
$ git clone git@github.com:kuznetsb/vpn_service.git
```
<br />

> 👉 Configure environmental variables
```bash
$ create .env file in project directory
$ Use default.env as template and copy all those DB variables to .env
$ fill DB variables with your values in .env file (exmaple: POSTGRES_DB=app)
```
Now your Postgres database will be configured properly

<br />

> 👉 Run docker-compose

```bash
$ docker-compose up
```
