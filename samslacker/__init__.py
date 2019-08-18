import json

import boto3

from samslacker.resources import Events

api_base = 'https://slacker.kipwise.com/api'
api_version = 'v1'
token = None
project = None


def event(_name, *args, **kwargs):
    if token is None:
        raise Exception('Please specify samslacker.token')

    data = {
        'event': _name,
        'arguments': kwargs
    }

    if project is not None:
        data['project_id'] = project

    sns_resource = boto3.resource('sns', region_name=aws_region)
    return sns_resource.Topic(sns_arn).publish(
        Message=json.dumps(data),
    )
