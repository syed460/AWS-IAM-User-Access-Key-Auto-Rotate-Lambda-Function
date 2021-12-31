#!/bin/python3

import json, csv
import boto3
from pprint import pprint
from datetime import datetime, timedelta
import subprocess, os
import urllib3


User_Name='user_account'
Day=80

def lambda_handler(event, context):

    iam_cli = boto3.client(service_name='iam')

    paginator = iam_cli.get_paginator('list_access_keys')

    x=1
    #print(paginator)
    for response in paginator.paginate(UserName=User_Name):
        #pprint(response['AccessKeyMetadata'])
        for each in response['AccessKeyMetadata']:
            #print(each['AccessKeyId'])
            Access_Key=each['AccessKeyId']
            CreateTime=each['CreateDate'].strftime("%m/%d/%Y")
            print(f"Key Created Date: {CreateTime}")
            utc_now = datetime.utcnow()
            ist_now = (utc_now + timedelta(hours=5,minutes=30)).strftime("%m/%d/%Y")
            print(f"IST Time now: {ist_now}")
            age = (datetime.strptime(ist_now, "%m/%d/%Y") - datetime.strptime(CreateTime, "%m/%d/%Y"))
            if age.days >= Day:
                print("Access key has reached 80 Days since it is creaetd. Hence, key will be dactivated")
                iam_cli.update_access_key(
                    AccessKeyId=Access_Key,
                    Status='Inactive',
                    UserName=User_Name
                )
            else:
                print(f"Age of the Key is only {age.days} days")
            print(f"====={x} key is validated======")
            x+=1
