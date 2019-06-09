# elivepatch-server
Flexible Distributed Linux Kernel Live Patching


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
