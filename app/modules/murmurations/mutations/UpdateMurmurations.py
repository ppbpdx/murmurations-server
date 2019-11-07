import datetime
import os

import requests
from box import Box
from graphene import Mutation, Boolean, String

from app.models.Model import Record

URL = os.environ.get('MURMURATION_INDEX_URL', 'https://murmurations.network/api/index')


class UpdateRecords(Mutation):
    ok = Boolean(description="Request status")
    message = String(description="Request message")

    class Input:
        node_type = String(description="Type of Node to Update")

    def mutate(self, info, **kwargs):
        update_local_db()
        return UpdateRecords(ok="ok", message="Database updated")


def update_local_db():
    payload = 'action=get_nodes'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", URL, headers=headers, data=payload)

    for (r) in response.json():
        r = Box(r, camel_killer_box=True)
        record = Record(
            name=r.get('name'),
            url=r.get('url'),
            api_url=r.get('api_url'),
            updated=datetime.datetime.fromtimestamp(r.get('updated')),
            node_types=r.get('nodeTypes'),
            location=r.get('location'),
            lat=r.get('lat'),
            long=r.get('long')
        )

        record.save_record()

    print(response.text.encode('utf8'))
