# Lawtech

This repository will contain the sources for building the backend of the Lawtech project


### Tech

* [Python 3](https://www.python.org/)
* [Django](https://www.djangoproject.com)
* [Docker](https://www.docker.com/)


## Version
Status: Development

Start date: 08/01/2020

### How to run
* start project with docker (make sure you have already install docker and docker-compose. If not, install via this [tutorial](https://docs.docker.com/compose/install/))
    ```sh
    $ docker-compose up -d    
    ```

### Populate database:
* run 
    ```sh
    $ docker-compose run --rm web python3 manage.py makemigrations
    $ docker-compose run --rm web python3 manage.py migrate 
    ```
* to reapply migrations, remove all containers, images, volumes, networks
and rerun above commands.
    ```sh
    $ docker system prune -a
    $ docker container stop {container name}
    $ docker container rm {container name}
    $ docker image prune -a
    $ docker volume prune
    $ docker network prune
    ```
