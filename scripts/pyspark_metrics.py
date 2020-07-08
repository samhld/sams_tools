import json
import os
import requests as re
import cProfile

import time


spark_apps_url = os.environ.get('SPARK_URL')
# spark_apps_url = "https://4ed059c6e07eeedd59f9ef858018349a.m.pipedream.net"

def get_app_ids():
    # returns list of appIDs to be used for generating endpoints
    r = re.get(spark_apps_url)
    app = App()
    appsJSON = r.json()
    appIDs = [app['id'] for app in appsJSON]
    return appIDs

def get_jobs(appID: str):
    # returns list of job dict from app by appID
    jobsJSON = re.get(f"{spark_apps_url}/{appID}/jobs").json()
    jobs = [Job(appID,job) for job in jobsJSON]
    return jobs

class App:
    def __init__(self):
        pass

class Job:
    def __init__(self, appID, job: dict):
        self.appID = appID
        self.jobID = job['jobId']
        self.name = job['name']
        self.submissionTime = job['submissionTime']
        self.completionTime = job['completionTime']
        self.status = job['status']
        self.numTasks = job['numTasks']
        self.numActiveTasks = job['numActiveTasks']
        self.numSkippedTasks = job['numSkippedTasks']
        self.numKilledTasks = job['numKilledTasks']


totalJobs = []
for appID in get_app_ids():
    for job in get_jobs(appID):
        totalJobs.append(job)

jobPoints = []
for job in totalJobs:
    jobPoints.append(f"spark_jobs,app_id={job.appID},name={job.name} submission_time={job.submissionTime},\
completionTime={job.completionTime},status={job.status},tasks={job.numTasks},app_id={job.appID},\
active_tasks={job.numActiveTasks},skipped_tasks={job.numSkippedTasks},killed_tasks={job.numKilledTasks} {time.time_ns()}")


for point in jobPoints:
    print(point)
