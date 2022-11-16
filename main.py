from fastapi import FastAPI, Query
import json
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Union,List

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def json_data_by_type(type: List[Union[str, None]] = Query(default=None)):
    with open('search.json',mode='r') as myfile:
        json_data = json.load(myfile)
        data_arr = []
        for i in json_data:
            if type is not None:
                for q in type:
                    if q == 'category':
                        data_arr.append(i['category'])
                    if q == 'description':
                        data_arr.append(i['description'])
                    if q == 'next_inspection':
                        data_arr.append(i['next_inspection'])
                    if q == 'operating_manager' and i.get('operating_manager', None) is not None:
                        data_arr.append(i['operating_manager'])
                    if q == 'operator':
                        data_arr.append(i['operator'])
                    if q == 'ordz':
                        data_arr.append(i['ordz'])
                    if q == 'site':
                        data_arr.append(i['site'])
            else:
                operator = i["operator"]
                if i.get("operating_manager",None) is not None:
                    operating_manager = i["operating_manager"]
                    data_arr.append(operating_manager)
                site = i["site"]
                ordz = i["ordz"]
                category = i["category"]
                description = i["description"]
                next_inspection = i["next_inspection"]
                data_arr.extend((operator, site, ordz, category, description ,next_inspection))
        return data_arr