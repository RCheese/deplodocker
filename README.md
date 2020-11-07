# DEPLODOCKER
___________
[![PyPI version](https://badge.fury.io/py/deplodocker.svg)](https://badge.fury.io/py/deplodocker)
___________

### Why?

Poetry and others python dependency managers has no cozy interface to communicate with requirements.
Some of them has no methods for export extras or extras without main requirements.
Some of them has no possibilities to use anither format excluding `requirements.txt`.
This project aims to fix this problem.  


### Basic usage

```shell script
>>> deplodocker --help
Usage: deplodocker [OPTIONS] [SRC]

  Select lock file to work with or use stdin as source

Options:
  -d, --dst FILENAME        result file
  -f, --input-format TEXT   format of input lock file
  -o, --output-format TEXT  format of output file
  --help                    Show this message and exit.
```

```shell script
>>> deplodocker poetry.lock
### MAIN
click==7.1.2
toml==0.10.2
### DEV
appdirs==1.4.4
atomicwrites==1.4.0
attrs==20.3.0
black==20.8b1
...
### SPEEDUPS
orjson==3.4.3
```

```shell script
>>> deplodocker poetry.lock -f poetry -o yaml
    dev:
      appdirs: 1.4.4
      atomicwrites: 1.4.0
      attrs: 20.3.0
      black: 20.8b1
      ...
    main:
      click: 7.1.2
      toml: 0.10.2
    speedups:
      orjson: 3.4.3
```

```shell script
>>> deplodocker poetry.lock -f poetry -o json
{"main":{"click":"7.1.2","toml":"0.10.2"},"dev":{"appdirs":"1.4.4","atomicwrites":"1.4.0","attrs":"20.3.0","black":"20.8b1","cfgv":"3.2.0","colorama":"0.4.4","coverage":"5.3","distlib":"0.3.1","filelock":"3.0.12","identify":"1.5.9","iniconfig":"1.1.1","isort":"5.6.4","mypy-extensions":"0.4.3","nodeenv":"1.5.0","packaging":"20.4","pathspec":"0.8.0","pluggy":"0.13.1","pre-commit":"2.8.2","py":"1.9.0","pyparsing":"2.4.7","pytest":"6.1.2","pytest-cov":"2.10.1","pyyaml":"5.3.1","regex":"2020.10.28","six":"1.15.0","typed-ast":"1.4.1","typing-extensions":"3.7.4.3","virtualenv":"20.1.0"},"speedups":{"orjson":"3.4.3"}}
```

Also you can use `stdin` as input and choose destination file trough arguments
```shell script
>>> cat poetry.lock | deplodocker poetry.lock -d requirements.json -f poetry -o json
```

<a href="https://www.buymeacoffee.com/RussianCheese" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/arial-violet.png" alt="Buy Me A Coffee" style="height: 51px !important;width: 217px !important;" ></a>