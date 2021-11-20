Download forecast data for Aurora Borealis and Aurora Australis from the National Weather Service

## Installation

```bash
pipenv install nws-aurora
```

## Command-line usage

```bash
```

Download data from the National Weather Service.

```bash
nwsaurora 
```

## Python usage

Import the library.

```python
>>> import nws_aurora
>>> 
```

## Contributing

Install dependencies for development.

```bash
pipenv install --dev
```

Run tests.

```bash
make test
```

Shipping new version to PyPI.

```bash
make ship
```

## Developing the CLI

The command-line interface is implemented using Click and setuptools. To install it locally for development inside your virtual environment, run the following installation command, as prescribed by the [Click documentation](https://click.palletsprojects.com/en/7.x/setuptools/#setuptools-integration).

```bash
pip install --editable .
```
