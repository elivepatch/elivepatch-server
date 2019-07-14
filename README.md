# elivepatch-server
[![Build Status](https://travis-ci.org/gentoo/elivepatch-server.svg?branch=master)](https://travis-ci.org/gentoo/elivepatch-server)
[![Maintainability](https://api.codeclimate.com/v1/badges/d79ff85d840722dbc9d6/maintainability)](https://codeclimate.com/github/gentoo/elivepatch-server/maintainability)
[![Docker Pulls](https://img.shields.io/docker/pulls/alice2f/elivepatch-server.svg?style=plastic)](https://hub.docker.com/r/alice2f/elivepatch-server)
[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/alice2f/elivepatch-server.svg)](https://hub.docker.com/r/alice2f/elivepatch-server)

Flexible Distributed Linux Kernel Live Patching

## System Dependencies
`elivepatch-server` needs the correct toolchain to build a Linux Kernel and the following software:
- [kpatch](https://github.com/dynup/kpatch)
- [git](https://git-scm.com/)

## Setup
`elivepatch-server` is a [flask](https://www.palletsprojects.com/p/flask/)-based application.

You can use [virtualenv](https://virtualenv.pypa.io/en/stable/) to have a separate python3 environment.
``` sh
$ cd elivepatch-server
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements
```

``` sh
$ python elivepatch-server
```

Will run the server using [werkzeug](https://palletsprojects.com/p/werkzeug/)

## API

- Endpoint root: /elivepatch/api/
- agent: /elivepatch/api/v1.0/agent
- send_livepatch: /elivepatch/api/v1.0/send_livepatch
- GetFiles: /elivepatch/api/v1.0/get_files

More information on the REST API is [here](docs/API.md)

## Development

You can use the [docker image](https://github.com/elivepatch/elivepatch-docker) to test your changes without the risk of damaging your system. 

Follow the provided [instructions](https://github.com/elivepatch/elivepatch-docker#basic-development) to set it up.
