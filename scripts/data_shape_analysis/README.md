# For analyzing InfluxDB input data

As InfluxDB is a schema-on-write database, it is important to understand and optimize the format and shape of data that you are writing to it.

By analyzing your data before it is written to InfluxDB, you can optimize and future proof your schema.

## Requires:

- [ ] Python 3.7+
- [ ] Matplotlib

For DataFrame functionality:
- [ ] Pandas
- [ ] Numpy

## Usage:

### IPython Notebook:

Import the Plotter() class: `from data_shape import Plotter`

Initialize an instance of Plotter with a block of text (*will support files later*): `plotter = Plotter(text)`

### Terminal:

Clone this repo.

In a directory you want to work in--and if you want to run in a VM--run: `pipenv install --ignore-pipfile`



### Web UI (roadmap?):


### To do:

- [ ] Add support for measurement, tag, field sizes (as opposed to counts) and create statistic description of that as well--add dict of this to description dict / row to Dataframe
- [ ] Cleanup bar plot
- [ ] Histogram support (needed?)