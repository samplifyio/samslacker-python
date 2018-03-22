import json

import boto3

from samslacker.resources import Events

api_base = 'https://samplify.io/slacker/api'
sns_arn = 'arn:aws:sns:us-east-1:319868825377:sam-slacker-event-created'
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

    sns_resource = boto3.resource('sns')
    return sns_resource.Topic(sns_arn).publish(
        Message=json.dumps(data),
    )
