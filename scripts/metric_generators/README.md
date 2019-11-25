# This application generates metrics in a format and method determined by the user

## Requires:
* Python 3.6+

## Not Yet Implemented:
* variables.env
* gen_config.py
* kafka_producer_metric_gen.py

(Not sure how I'm going to implement these for the best UX yet)

## How To Use:
Clone this repository.  If/when you're in the directory `/metric_generators`, run `python3 generator.py <flags>` (flags are listed in the How To Use section)


## Possible Formats:
* Influx
* Graphite
* Prometheus

These are called with the `--format` flag when running the program; i.e., `python3 generator.py --format graphite`

## Possible Protocols:
* HTTP
* UDP

These are called with the `--protocol` flag
## Batching:
* Batch size
* Number of batches
* Interval-->sampling interval or time between samples.  This will manifest as time between timestamps of batches

These are called with the `--batch_size`, `--num_batches`, and `--interval` flags, respectively.

## Still To Do:
* Add support for writing to Kafka
* Allow for writing a batch at a time instead of the current of aggregating all batches and sending as one large batch
* Add `--output` flag to determine whether the program writes to Influx1, Influx2, or Kafka
* Use the `variables.env` file to allow for changing of static variables (regions, apps, hosts, addr, port)
