Download forecast data for Aurora Borealis and Aurora Australis from the National Weather Service

Hourly scrapes powered by a GitHub Action are stored in the `data` directory.

## Installation

```bash
pipenv install nws-aurora
```

## Command-line usage

```bash
Usage: nwsaurora [OPTIONS] COMMAND [ARGS]...

  A command-line interface for downloading forecast data for Aurora Borealis
  and Aurora Australis from the National Weather Service

Options:
  --help  Show this message and exit.

Commands:
  forecast  Get Ovation Aurora Short Term Forecast data
  grid      Get auroral data in a gridded format for the entire Earth
  images    Ovation model images from the last 24 hours
```

Download data from the National Weather Service.

```bash
nwsaurora images --pole=north
nwsaurora images --pole=south
nwsaurora images --pole=north --latest
nwsaurora images --pole=south --latest
nwsaurora grid
nwsaurora forecast
```

## Python usage

Import the library.

```python
>>> import nws_aurora
>>> nws_aurora.get_images('north')
>>> nws_aurora.get_images('south')
>>> nws_aurora.get_latest_image('north')
>>> nws_aurora.get_latest_image('south')
>>> nws_aurora.grid()
>>> nws_aurora.forecast()

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
