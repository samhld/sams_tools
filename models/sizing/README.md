## Description
This is an app for end-to-end building of a model to predict InfluxEnterprise cluster sizing based on user-provided inputs.  It pulls monitoring stats from InfluxCloud1 that are needed for training and testing the predictive model and supplies a Python notebook for doing the machine learning.

The data pulled is currently across the most recent minute (at time of query) until decided otherwise.

## Data attributes included (features)
All of the below metrics are per nod per cluster
* cpu usage
* mem used/availble
* points written per min
* queries executed per min
* diskio
  - bytes in/out
  - read/write counts
* system
  - num cores
  - cpu load
* http requests
  - read/write


Possible features to derive:
* cpu usage normalized for cpu count
* mem usage normalized for mem available



