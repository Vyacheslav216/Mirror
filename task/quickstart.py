#!/usr/bin/python3
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time
from datetime import date, timedelta
# If modifying these scopes, delete the file token.pickle.


def main():
    SCOPES = ['https://www.googleapis.com/auth/tasks.readonly']
    """Shows basic usage of the Tasks API.
    Prints the title and ID of the first 10 task lists.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('tasks', 'v1', credentials=creds)

    # Call the Tasks API
    results = service.tasklists().list(maxResults=10).execute()
    items = results.get('items', [])
    listtask=[]
    listtask.append([])
    i=-1
    if not items:
        print('No task lists found.')
    else:
        for item in items:
            i+=1
           # print('Task lists:')
          #  print(u'{0} ({1})'.format(item['title'], item['id']))
           # print(u'{0}'.format(item['title']))
            listtask.append([])
           # listtask[i].append(u'{0}'.format(item['title']))
            s=u'{0}'.format(item['id'])
           # taskd = service.tasks().list(tasklist=s,dueMin="2019-05-04T10:57:00.000-08:00").execute()
            newdate=date.today()+timedelta(days=-1)
            taskd = service.tasks().list(tasklist=s,dueMin=(newdate.strftime('%Y-%m-%d')+"T10:57:00.000-00:00"),dueMax=time.strftime('%Y-%m-%d')+"T10:57:00.000-00:00").execute()
            #tasks = service.tasks().list(tasklist=s).execute()
            #for task in tasks['items']:
                #print (task['title'])
            #    listtask[i].append(task['title'])
            
            try:
                for task in taskd['items']:
                #print (task['title'])
                    print(str(task['title']))
                    s="•"+str(task['title'])
                    listtask[i].append(s)
            except:
                pass
            #print('\n')
        return(listtask)   
if __name__ == '__main__':
    main()