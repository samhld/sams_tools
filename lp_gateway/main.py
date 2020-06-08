import json_parser, line_parser
from fastapi import FastAPI

gateway = FastAPI()

# add async and await where needed (later)
# for later, `< >` indicate to fill with objects I create
@gateway.get("/")
def root():
    return {"<key>": "<value>"}

@gateway.post("/write/")
def write():
    return "this is the write endpoint"
    # create a write request to backend


    # return success if write was successful

@gateway.get("/read")
def read():
    return "this is the read endpoint"