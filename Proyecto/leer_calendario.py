import datetime
import pyttsx3
import os.path
hora_actual=datetime.datetime.now()
hora_formateada = hora_actual.strftime('%y/%m/%d %H:%M')
import comunicacionserie

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def main():
  def hablar(a:str):
        engine = pyttsx3.init() 
        engine.setProperty("rate", 150)
        text = a
        engine.say(text)
        engine.runAndWait()
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "apiclara.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    now=now.split(':')
    now= now[0]+":00:00.000000Z"
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="clara2006f@gmail.com",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    for event in events:
      start = event["start"].get("dateTime")
      start= start.split('T')
      fecha=start[0].split('-')
      anio=fecha[0].split('0')
      anio=anio[1]
      fecha=anio+'/'+fecha[1]+'/'+fecha[2]
      start=start[1].split('-')
      start=start[0].split(':')
      start=start[0] +":"+ start[1]
      start=fecha+ " "+ start
      print(start)
      print(hora_formateada)
      print(event["summary"])
      if start==hora_formateada:
        print(event["summary"])
        comunicacionserie.comunicacionserial(event["summary"])
        hablar(event["description"])

  except HttpError as error:
    print(f"An error occurred: {error}")
