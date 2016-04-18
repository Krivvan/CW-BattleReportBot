# Make sure this script starts at the period just after each ceasefire period (T05-00 at the moment)
#SUBREDDIT = 'krivvanstestsubreddit'
SUBREDDIT = 'outreachhpg'

import time, datetime

class Factions():
  None_ID             =  "0"
  None2_ID            =  "3"
  Comstar_ID          =  "1"
  Davion_ID           =  "5"
  Liao_ID             =  "7"
  Marik_ID            =  "8"
  Steiner_ID          = "10"
  Rasalhague_ID       =  "9"
  Kurita_ID           =  "6"
  ClanJadeFalcon_ID   = "12"
  ClanWolf_ID         = "13"
  ClanGhostBear_ID    = "14"
  ClanSmokeJaguar_ID  = "11"
  IncludedFactions    = [Davion_ID, Liao_ID, Marik_ID, Steiner_ID, Rasalhague_ID, Kurita_ID, ClanJadeFalcon_ID, ClanWolf_ID, ClanGhostBear_ID, ClanSmokeJaguar_ID]
  IS_Factions         = [Davion_ID, Liao_ID, Marik_ID, Steiner_ID, Rasalhague_ID, Kurita_ID]
  Clan_Factions       = [ClanJadeFalcon_ID, ClanWolf_ID, ClanGhostBear_ID, ClanSmokeJaguar_ID]
  FullNames            = {None_ID:"None", None2_ID:"None", Comstar_ID:"Comstar", Davion_ID:"The Federated Suns", Liao_ID:"Capellan Confederation", Marik_ID:"Free Worlds League",\
                         Steiner_ID:"Lyran Commonwealth", Rasalhague_ID:"Free Rasalhague Republic", Kurita_ID:"Draconis Combine",\
                         ClanJadeFalcon_ID:"Clan Jade Falcon", ClanWolf_ID:"Clan Wolf", ClanGhostBear_ID:"Clan Ghost Bear", ClanSmokeJaguar_ID:"Clan Smoke Jaguar"}
  Initials             = {None_ID:"N/A", None2_ID:"N/A", Comstar_ID:"CS", Davion_ID:"FS", Liao_ID:"CC", Marik_ID:"FWL",\
                         Steiner_ID:"LC", Rasalhague_ID:"FRR", Kurita_ID:"DC",\
                         ClanJadeFalcon_ID:"CJF", ClanWolf_ID:"CW", ClanGhostBear_ID:"CGB", ClanSmokeJaguar_ID:"CSJ"}
  OriginalTotalPlanets = {Davion_ID:591, Liao_ID:121, Marik_ID:319, Steiner_ID:449, Rasalhague_ID:76, Kurita_ID:330,\
                         ClanJadeFalcon_ID:11, ClanWolf_ID:16, ClanGhostBear_ID:8, ClanSmokeJaguar_ID:5}
                         
                         

def loadJSON():
  import urllib
  import json

  d = datetime.datetime.utcnow()

  year = str(d.year + 1035)
  #month = str(02).zfill(2)
  month = str(d.month).zfill(2)
  #day = str(02).zfill(2)
  day = str(d.day).zfill(2)
  
  print day
  
  #currentURL = "https://static.mwomercs.com/data/cw/mapdata.json"
  currentURL = "https://static.mwomercs.com/data/cw/mapdata-" + year + "-" + month + "-" + day + "T22-15" + ".json"
  jsonurl = urllib.urlopen(currentURL)
  currentData = json.loads(jsonurl.read())

  pastURL = "https://static.mwomercs.com/data/cw/mapdata-" + year + "-" + month + "-" + day + "T22-00" + ".json"
  jsonurl = urllib.urlopen(pastURL)
  pastData = json.loads(jsonurl.read())

  date = "**" + "EU - 22:00 UTC - " + month + "/" + day + "/" + year + "**  \n\n"
  
  return (currentData, pastData, date)
  
def createPostContent():
  currentData, pastData, dateReport = loadJSON()
  
  defenseReportList = []
  defenseTableList = []
  attackReportList = []
  attackTableList = []
  nothingReport = "Nothing on "
  netChange    =  {Factions.Davion_ID:0, Factions.Liao_ID:0, Factions.Marik_ID:0, Factions.Steiner_ID:0, Factions.Rasalhague_ID:0, Factions.Kurita_ID:0,\
                 Factions.ClanJadeFalcon_ID:0, Factions.ClanWolf_ID:0, Factions.ClanGhostBear_ID:0, Factions.ClanSmokeJaguar_ID:0}
  totalPlanets =  {Factions.Davion_ID:0, Factions.Liao_ID:0, Factions.Marik_ID:0, Factions.Steiner_ID:0, Factions.Rasalhague_ID:0, Factions.Kurita_ID:0,\
                 Factions.ClanJadeFalcon_ID:0, Factions.ClanWolf_ID:0, Factions.ClanGhostBear_ID:0, Factions.ClanSmokeJaguar_ID:0}    
  actualTotalPlanets =  {Factions.Davion_ID:0, Factions.Liao_ID:0, Factions.Marik_ID:0, Factions.Steiner_ID:0, Factions.Rasalhague_ID:0, Factions.Kurita_ID:0,\
               Factions.ClanJadeFalcon_ID:0, Factions.ClanWolf_ID:0, Factions.ClanGhostBear_ID:0, Factions.ClanSmokeJaguar_ID:0}    
  
  for id in range (1,2241):
    if (str(id) in pastData):
      if (pastData[str(id)]["contested"] == "1"):
        if (pastData[str(id)]["owner"]["id"] == currentData[str(id)]["owner"]["id"]):
          planetName = pastData[str(id)]["name"]
          defender = Factions.FullNames[pastData[str(id)]["owner"]["id"]]
          attacker = Factions.FullNames[pastData[str(id)]["invading"]["id"]]
          defenderInitials = Factions.Initials[pastData[str(id)]["owner"]["id"]]
          attackerInitials = Factions.Initials[pastData[str(id)]["invading"]["id"]]
          attackerWins = sum( [bin(int(item)).count("1") for item in pastData[str(id)]["territories"]] )
          if (attackerWins > 0):
            defenseReportLine = defender + " holds " + attacker + " to " + str(attackerWins) + " on " + planetName + ".\n\n"
            defenseReportList.append(defenseReportLine)
            defenseTableLine = defenderInitials + "|" + planetName + "|" + attackerInitials + "\n"
            defenseTableList.append(defenseTableLine)
          else:
            nothingReport = nothingReport + planetName + " (" + attackerInitials + " &gt; " + defenderInitials + "), "
            
        elif (pastData[str(id)]["owner"]["id"] != currentData[str(id)]["owner"]["id"]):
          planetName = pastData[str(id)]["name"]
          defender = Factions.FullNames[pastData[str(id)]["owner"]["id"]]
          attacker = Factions.FullNames[pastData[str(id)]["invading"]["id"]]
          defenderInitials = Factions.Initials[pastData[str(id)]["owner"]["id"]]
          attackerInitials = Factions.Initials[pastData[str(id)]["invading"]["id"]]          
          attackReportLine = attacker + " takes " + planetName + " from " + defender + "!**\n\n"
          attackReportList.append(attackReportLine)
          attackTableLine = attackerInitials + "|" + planetName + "|" + defenderInitials + "\n"
          attackTableList.append(attackTableLine)
          
          if (id != 1):        
            invaderID = pastData[str(id)]["invading"]["id"]
            if (invaderID in Factions.IncludedFactions):
              netChange[invaderID] = netChange[invaderID] + 1
              netChange[pastData[str(id)]["owner"]["id"]] = netChange[pastData[str(id)]["owner"]["id"]] - 1
    
  if (len(attackReportList) > 0):
    attackReport = "**" + '**'.join(sorted(attackReportList, key=lambda x:x[:2]))
  else:
    attackReport = "" + '**'.join(sorted(attackReportList, key=lambda x:x[:2]))
  
  attackTable = "Winner|Planet|Loser\n"
  attackTable = attackTable + "------|------|-----\n"
  attackTable = attackTable + ''.join(sorted(attackTableList, key=lambda x:x[:2]))
  
  defenseReport = ''.join(sorted(defenseReportList, key=lambda x:x[:2]))
  
  defenseTable = "Defender|Planet|Attacker\n"
  defenseTable = defenseTable + "------|------|-----\n"
  defenseTable = defenseTable + ''.join(sorted(defenseTableList, key=lambda x:x[:2]))        
  
  nothingReport = nothingReport[:-2]
  
  factionNetChangeOrder = sorted(netChange, key=netChange.get)
  netChangeString = ""
  for id in reversed(factionNetChangeOrder):
    factionNet = netChange[id]
    factionNetString = ""
    if (factionNet > 0):
      factionNetString = "+" + str(factionNet)
    else:
      factionNetString = str(factionNet)
    netChangeString = netChangeString + "**" + Factions.Initials[id] + " " + factionNetString + "**" + "\n\n"
  
  totalPlanetsStringHeader = ""
  totalPlanetsNetString = ""
  actualTotalPlanetsStringHeader = ""
  actualTotalPlanetsNetString = ""  
  #Inefficient to do this again, but it's a bot that runs at most a few times a day, clarity is more important
  for id in range (1,2241):
    if (str(id) in pastData):
      factionID = currentData[str(id)]["owner"]["id"]
      if (factionID in Factions.IncludedFactions):
        totalPlanets[factionID] = totalPlanets[factionID] + 1
  for factionID, total in totalPlanets.iteritems():
    actualTotalPlanets[factionID] = total
    totalPlanets[factionID] = total - Factions.OriginalTotalPlanets[factionID]
  actualTotalPlanetsOrder = sorted(actualTotalPlanets, key=actualTotalPlanets.get)
  totalPlanetsOrder = sorted(totalPlanets, key=totalPlanets.get)
  
  for id in reversed(totalPlanetsOrder):
    factionTotalPlanets = totalPlanets[id]
    factionTotalPlanetsString = ""
    if (factionTotalPlanets > 0):
      factionTotalPlanetsString = "+" + str(factionTotalPlanets)
    else:
      factionTotalPlanetsString = str(factionTotalPlanets)    
    totalPlanetsStringHeader = totalPlanetsStringHeader + Factions.Initials[id] + "|"
    totalPlanetsNetString = totalPlanetsNetString + factionTotalPlanetsString + "|"
	
  for id in reversed(actualTotalPlanetsOrder):
    factionActualTotalPlanets = actualTotalPlanets[id]
    factionActualTotalPlanetsString = ""
    factionActualTotalPlanetsString = str(factionActualTotalPlanets)    
    actualTotalPlanetsStringHeader = actualTotalPlanetsStringHeader + Factions.Initials[id] + "|"
    actualTotalPlanetsNetString = actualTotalPlanetsNetString + factionActualTotalPlanetsString + "|"	
    
  totalPlanetsStringHeader = totalPlanetsStringHeader[:-1]
  totalPlanetsNetString = totalPlanetsNetString[:-1]
  totalPlanetsString = totalPlanetsStringHeader + "\n" + "---|---|---|---|---|---|---|---|---|---\n" + totalPlanetsNetString + "\n\n"
  
  actualTotalPlanetsStringHeader = actualTotalPlanetsStringHeader[:-1]
  actualTotalPlanetsNetString = actualTotalPlanetsNetString[:-1]
  actualTotalPlanetsString = actualTotalPlanetsStringHeader + "\n" + "---|---|---|---|---|---|---|---|---|---\n" + actualTotalPlanetsNetString + "\n\n"
  
  line = "--------------------------------------------------------\n\n"
  
  report = line + dateReport + attackReport + attackTable + "\n\n" + defenseReport + defenseTable + "\n\n" + nothingReport + "\n\n\n" + netChangeString + "Net change:\n\n" + totalPlanetsString + "Total:\n\n" + actualTotalPlanetsString + "\n"
  
  return report

# obtain OAuth2 access token
def getAccessToken():
  import requests
  import requests.auth
  import praw

  response = requests.post("https://www.reddit.com/api/v1/access_token",
    # client id and client secret are obtained via your reddit account
    auth = requests.auth.HTTPBasicAuth("sVYWpbgi_JYxPg", "YfeShpprgQ2YIHqg3w2JYVkQneo"),
    # provide your reddit user id and password
    data = {"grant_type": "password", "username": USERNAME, "password": PASSWORD},
    # you MUST provide custom User-Agent header in the request to play nicely with Reddit API guidelines
    headers = {"User-Agent": "CW Battle Report 0.2: Script run by /u/Krivvan that makes submissions giving updates for the community warfare feature of the game Mechwarrior Online"})
  response = dict(response.json())
  print response
  return response["access_token"]     
  
def editRedditPost():
  import praw

  user = praw.Reddit('CW Battle Report 0.2: Run by /u/Krivvan that makes submissions giving updates for the community warfare feature of the game Mechwarrior Online')
  user.set_oauth_app_info(client_id='NotARealClientID', client_secret='NotARealClientSeceret', redirect_uri='http://127.0.0.1:65010/authorize_callback')
  user.set_access_credentials(set(["identity", "save", "edit", "mysubreddits", "privatemessages", "read", "submit", "subscribe", "history"]), getAccessToken())
  #user.login(USERNAME, PASSWORD)
  
  currentDate = datetime.datetime.utcnow()
  
  #First
  #startDate = datetime.datetime(2014, 12, 11, 5, 00, 00, 00000)
  
  #Second
  #startDate = datetime.datetime(2015, 4, 30, 5, 00, 00, 00000)
  
  #Third
  startDate = datetime.datetime(2015, 12, 10, 5, 00, 00, 00000)   
  
  day = (currentDate - startDate).days
  
  repostFound = False

  body = createPostContent()
  authenticated_user = user.get_me()
  previouslyCreatedPost = authenticated_user.get_saved('new').next()
  previousBody = previouslyCreatedPost.selftext.encode('ascii').replace('amp;', '')
  previousBodyTruncated = previousBody[:(previousBody.find('[**Link to'))]
  previousBodyLink = previousBody[(previousBody.find('[**Link to')):(previousBody.find('^^Message'))]
  body = previousBodyTruncated + body + previousBodyLink
  body = body + "^^Message ^^/u/Krivvan ^^if ^^something ^^is ^^wrong ^^with ^^this ^^automatically ^^generated ^^report.\n\n"
  
  previouslyCreatedPost.edit(body)


def main():

  editRedditPost()

if __name__ == '__main__':
    main()