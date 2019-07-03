import requests as re

r = re.get('http://localhost:4040/api/v1/applications')
appJSON = r.json()

# collect application IDs into a list to be iterated over later
# because they need to be fed to other API request URLs
appIDs = [item['id'] for item in appJSON]

# collect list of jobs api urls by each appID
appJobsURLs = ['http://localhost:4040/api/v1/applications/'+appIDs[i]+'/jobs' for i,id in enumerate(appIDs)]
print(appJobsURLs)

# loop through and send requests to every url in list of jobs urls
jobsJSONlist = []
for jobURL in appJobsURLs:
    req = re.get(jobURL)
    jobsJSONlist.append(req.json())
print(f"Jobs data: {jobsJSONlist}") # if any


# also collect job IDs for details on certain jobs
try:
    jobIDs = [job[i]['id'] for i,job in enumerate(jobsJSONlist)]
    print(f"Job IDs: {jobIDs}")

    # collect list of job ID api urls by each appID-jobID
    appJobIDURLs = [appJobsURLs+jobIDs[i] for i,id in enumrate(appJobsURLs)]
    print(f"App job URLs: {appJobIDURLs}")

    # collect JSON from each given job by the job's respective URL
    for url in appJobIDURLS:
        req = re.get(url)
        print(req.json)


except NameError:
    print("NameError occured likely because no job IDs to print")
except IndexError:
    print("IndexError occured likely because job list is empty")

# collect list of executor api urls by each appID
appExecutorURLs = ['http://localhost:4040/api/v1/applications/'+appIDs[i]+'/executors' for i,id in enumerate(appIDs)]
print(appExecutorURLs)

# loop through and send requests to every url in list of executor urls
executorJSONlist = []
for executorURL in appExecutorURLs:
    req = re.get(executorURL)
    executorJSONlist.append(req.json())
print(f"Executors data: {executorJSONlist}") # if any

# also collect executor IDs for details on certain executors
try:
    executorIDs = [exec[i]['id'] for i,exec in enumerate(executorJSONlist)]
    print(f"Executor IDs: {executorIDs}")
    # collect list of executor ID api urls by each appID-executorID
    appExecutorIDURLs = [appExecutorURLs[i] + '/' + executorIDs[i] + '/threads' for i,id in enumerate(appExecutorURLs)]
    print(f"App executor URLs: {appExecutorIDURLs}")

    # collect JSON from each given executor by the executor's respective URL
    for url in appExecutorIDURLs:
        req = re.get(url)
        print(req.json)

except NameError:
    print("NameError occured likely because no executor IDs to print")
except IndexError:
    print("IndexError occured likely because executor list is empty")


