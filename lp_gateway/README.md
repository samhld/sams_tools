# The Line Protocol Parsing Gateway

## This is a service/daemon that can run locally or remotely designed to help transform data of a user-specified format into InfluxDB Line Protocol according to the schema you want from it

### To do this, the LPPG does a few things:
* Take input from user about what schema they will use
    ** could be a configuration file change, a runtime flag, etc.
* Take information what keywords should be Measurements, Tags, Fields
    ** could be a configuration file change or possibly a user-created json/yaml/toml/xml/ini file from which LGGP reads
* Read the incoming text-based objects/requests and construct optimal line protocol.  Methods of getting data in