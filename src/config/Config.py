import json
import os

def getServerConfig(): #Get server details from  Config file return server details in JSON format
  with open('../config/server.json', 'r') as server:
    jsonServerData = json.load(server)
    return jsonServerData

def getSystemConfig():  #Get system details from  system file return details in JSON format
  with open('../config/system.json', 'r') as system:
    jsonSystemData = json.load(system)
    return jsonSystemData

def getBrokerAppConfig():  #Get broker app details from  file return details in JSON format
  with open('../config/brokerapp.json', 'r') as brokerapp:
    jsonUserData = json.load(brokerapp)
    return jsonUserData

def getHolidays():  #Get Holidays list from Holidays file return details in JSON format
  with open('../config/holidays.json', 'r') as holidays:
    holidaysData = json.load(holidays)
    return holidaysData

def getTimestampsData():  #Get time stamp from server (instruments) and store timestamp in timestamp.json in file directory
  serverConfig = getServerConfig()
  timestampsFilePath = os.path.join(serverConfig['deployDir'], 'timestamps.json')
  if os.path.exists(timestampsFilePath) == False:
    return {}
  timestampsFile = open(timestampsFilePath, 'r')
  timestamps = json.loads(timestampsFile.read())
  return timestamps

def saveTimestampsData(timestamps = {}): #saves time stamp data to file
  serverConfig = getServerConfig()
  timestampsFilePath = os.path.join(serverConfig['deployDir'], 'timestamps.json')
  with open(timestampsFilePath, 'w') as timestampsFile:
    json.dump(timestamps, timestampsFile, indent=2)
  print("saved timestamps data to file " + timestampsFilePath)
