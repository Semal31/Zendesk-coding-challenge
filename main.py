import os 
import requests

from dotenv import load_dotenv
load_dotenv()

USER_NAME = os.environ.get("API_USER")
API_TOKEN = os.environ.get("API_TOKEN")

url = "https://zcc2793.zendesk.com/api/v2/tickets.json?page[size]=25"
r = requests.get(url, auth=(USER_NAME, API_TOKEN))
if r.status_code != 200:
  print("Cannot establish a connection to the api right now. Please check the authorization credentials or try again later")
  exit(1)
r = r.json()

done = False
mainPrompt = "Welcome to the ticket viewer V1\nThe options are as follows:\n    'h' to view this menu again\n    'a' to view all tickets\n    'i' to select an individual ticket to view\n    'q' to quit the application"
allTicketsPrompt1 = "'q' to stop viewing"
allTicketsPrompt2 = "'2' for the next page || 'q' to stop viewing"
allTicketsPrompt3 = "'1' for the previous page || '2' for the next page || 'q' to stop viewing"
allTicketsPrompt4 = "'1' for the previous page || 'q' to stop viewing"
individualTicketPrompt1 = "What is the id of the ticket you would like to view?"
individualTicketPrompt2 = "'1' to input another ticket id to view || 'q' to stop viewing"
options = ['h', 'a', 'i', 'q']
viewingAllTicketsOptions = ['1', 'q', '2']

while not done:
  print(mainPrompt)
  inputOption = input()
  while (inputOption not in options):
    print(mainPrompt)
    inputOption = input()
  if inputOption == options[3]:
    done = True
  elif inputOption == options[0]:
    continue
  elif inputOption == options[1]:
    pageCounter = 0
    viewingAllTickets = True
    while viewingAllTickets:
      print(f"{r['tickets'][0]['id']} \n")

      if pageCounter == 0 and not r['meta']['has_more']:
        print(allTicketsPrompt1)
        inputAllTickets = input()
        while inputAllTickets != viewingAllTicketsOptions[1]:
          print(allTicketsPrompt1)
          inputAllTickets = input()
        if inputAllTickets == viewingAllTicketsOptions[1]:
          viewingAllTickets = False

      elif pageCounter == 0 and r['meta']['has_more']:
        print(allTicketsPrompt2)
        inputAllTickets = input()
        while inputAllTickets not in viewingAllTicketsOptions[1:]:
          print(allTicketsPrompt2)
          inputAllTickets = input()
        if inputAllTickets == viewingAllTicketsOptions[1]:
          viewingAllTickets = False
        elif inputAllTickets == viewingAllTicketsOptions[2]:
          pageCounter += 1
          r = (requests.get(r["links"]["next"], auth=(USER_NAME, API_TOKEN))).json()
          continue

      elif pageCounter > 0 and r['meta']['has_more']:
        print(allTicketsPrompt3)
        inputAllTickets = input()
        while inputAllTickets not in viewingAllTicketsOptions:
          print(allTicketsPrompt3)
          inputAllTickets = input()
        if inputAllTickets == viewingAllTicketsOptions[1]:
          viewingAllTickets = False
        elif inputAllTickets == viewingAllTicketsOptions[2]:
          pageCounter += 1
          r = (requests.get(r["links"]["next"], auth=(USER_NAME, API_TOKEN))).json()
          continue
        elif inputAllTickets == viewingAllTicketsOptions[0]:
          pageCounter -= 1
          r = (requests.get(r["links"]["prev"], auth=(USER_NAME, API_TOKEN))).json()
          continue

      elif pageCounter > 0 and not r['meta']['has_more']:
        print(allTicketsPrompt4)
        inputAllTickets = input()
        while inputAllTickets not in viewingAllTicketsOptions[:2]:
          print(allTicketsPrompt4)
          inputAllTickets = input()
        if inputAllTickets == viewingAllTicketsOptions[1]:
          viewingAllTickets = False
        elif inputAllTickets == viewingAllTicketsOptions[0]:
          pageCounter -= 1
          r = (requests.get(r["links"]["prev"], auth=(USER_NAME, API_TOKEN))).json()
          continue
  elif inputOption == options[2]:
    viewingIndivTicket = True
    while viewingIndivTicket:
      print(individualTicketPrompt1)
      inputIndivTicket = input()
      while not inputIndivTicket.isdigit():
        print(individualTicketPrompt1)
        inputIndivTicket = input()
      url = f"https://zcc2793.zendesk.com/api/v2/search.json?query={inputIndivTicket}"
      r = (requests.get(url, auth=(USER_NAME, API_TOKEN))).json()
      print(f"{r} \n")
      print(individualTicketPrompt2)
      inputIndivTicket = input()
      while inputIndivTicket not in viewingAllTicketsOptions[:2]:
        print(individualTicketPrompt2)
        inputIndivTicket = input()
      if inputIndivTicket == viewingAllTicketsOptions[1]:
        viewingIndivTicket = False
      
