import json
import os
import requests as re
import cProfile

spark_apps_url = os.environ.get('SPARK_URL')
# spark_apps_url = "https://4ed059c6e07eeedd59f9ef858018349a.m.pipedream.net"

def get_app_ids():
    # returns list of appIDs to be used for generating endpoints
    r = re.get(spark_apps_url)
    appsJSON = r.json()
    appIDs = [app['id'] for app in appsJSON]
    return appIDs

def get_jobs(appID: str):
    # returns list of job dict from app by appID
    print(re.get(f"{spark_apps_url}/{appID}/jobs"))
    jobs = re.get(f"{spark_apps_url}/{appID}/jobs").json()
    return jobs

for appID in get_app_ids():
    print(get_jobs(appID))