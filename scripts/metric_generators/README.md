# This application generates metrics in a format and method determined by the user

## Possible Formats:
* Influx
* Graphite
* Prometheus

These are called with the `--format` flag when running the program; i.e., `python3 generator.py --format graphite`

## Possible protocols:
* HTTP
* UDP

These are called with the `--protocol` flag
## Batching:
* Batch size
* Number of batches
* Interval-->sampling interval or time between samples.  This will manifest as time between timestamps of batches

These are called with the `--batch_size`, `--num_batches`, and `--interval` flags, respectively.

## How to use:
    