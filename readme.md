### Getting started

![spirographs](spirographs.png)

create python virtual environment named `venv`

```shell
python -m venv './venv'
```

activate virtual environment with `source './venv/bin/activate'`

update pip

```shell
python -m pip install --upgrade pip setuptools wheel
```

install library `pystdlib`

```shell
python -m pip install git+ssh://git@github.com/ibqn/pystdlib.git
```

test that the library was installed correctly by executing the following command

```shell
python -c 'import pystdlib; print("ok")'
```

to deactivate venv run `deactivate`
