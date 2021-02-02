[![Build Status](https://travis-ci.com/lucasOlivio/droidio.svg?branch=master)](https://travis-ci.com/lucasOlivio/droidio)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)
[![License](https://img.shields.io/npm/l/react-native-smart-badge.svg)](https://github.com/lucasOlivio/droidio/blob/master/LICENSE)

Long live the Empire!

Droid.io is a project to help our allies in the best way we know, with a microservice to manage droids parts demands!
Only authenticated users can access and are able to create, edit, list and delete all his demands with ease.

Check out the project's [documentation](http://lucasOlivio.github.io/droidio/).

------------------------------------------------------------------------------------------------------------------------
# SERVER

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-windows/install/)
- [Docker](https://docs.docker.com/engine/install/)
- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Local Development

Start the dev server for local development:
```bash
docker-compose -f local.yml up
```

Run tests and tests coverage in container:

```bash
docker-compose -f local.yml run --rm server coverage run -m pytest
```

Run any command inside the docker container:

```bash
docker-compose -f local.yml run --rm server [command]
```
