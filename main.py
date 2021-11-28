import os 
import requests
from helper import *

from dotenv import load_dotenv
load_dotenv()

USER_NAME = os.environ.get("API_USER")
API_TOKEN = os.environ.get("API_TOKEN")
SUBDOMAIN = os.environ.get("SUBDOMAIN")
DIGIT = 'digit'

def getJsonData(link):
  return (requests.get(link, auth=(USER_NAME, API_TOKEN))).json()

def main():
  allTicketsUrl = f"https://{SUBDOMAIN}.zendesk.com/api/v2/tickets.json?page[size]=25"
  r = requests.get(allTicketsUrl, auth=(USER_NAME, API_TOKEN))
  if r.status_code != 200:
    print("Cannot establish a connection to the API right now. Please check the authorization credentials or try again later")
    exit(1)
  r = r.json()

  done = False
  mainPrompt = "Welcome to the ticket viewer V1\nThe options are as follows:\n    'a' to view all tickets\n    'i' to select an individual ticket to view\n    'q' to quit the application"
  mainOptions = ['a', 'i', 'q']
  allTicketsPrompt1 = "\n'q' to return to the main menu"
  allTicketsPrompt2 = "\n'2' for the next page || 'q' to return to the main menu"
  allTicketsPrompt3 = "\n'1' for the previous page || '2' for the next page || 'q' to return to the main menu"
  allTicketsPrompt4 = "\n'1' for the previous page || 'q' to return to the main menu"
  individualTicketPrompt1 = "\nWhat is the id of the ticket you would like to view?"
  individualTicketPrompt2 = "\nNo ticket with this id found."
  individualTicketPrompt3 = "\n'd' to view the description of the ticket || '1' to input another ticket id to view || 'q' to return to the main menu"
  individualTicketPrompt4 = "\n'1' to input another ticket id to view || 'q' to return to the main menu"
  viewingTicketsOptions = ['1', 'q', '2', 'd']

  while not done:
    inputOption = getInput(mainPrompt, mainOptions)

    # Quit application
    if inputOption == mainOptions[2]:
      done = True

    # View all tickets
    elif inputOption == mainOptions[0]:
      r = getJsonData(allTicketsUrl)
      pageCounter = 0
      viewingAllTickets = True
      while viewingAllTickets:
        printTickets(r['tickets'], True)

        # Only one page of tickets are available  
        if pageCounter == 0 and not r['meta']['has_more']:
          inputAllTickets = getInput(allTicketsPrompt1, viewingTicketsOptions[1])
          if inputAllTickets == viewingTicketsOptions[1]:
            viewingAllTickets = False

        # On the first page and more pages are available 
        elif pageCounter == 0 and r['meta']['has_more']:
          inputAllTickets = getInput(allTicketsPrompt2, viewingTicketsOptions[1:3])
          if inputAllTickets == viewingTicketsOptions[1]:
            viewingAllTickets = False
          elif inputAllTickets == viewingTicketsOptions[2]:
            pageCounter += 1
            r = getJsonData(r["links"]["next"])
            continue

        # Past the first page and more pages are available
        elif pageCounter > 0 and r['meta']['has_more']:
          inputAllTickets = getInput(allTicketsPrompt3, viewingTicketsOptions[:3])
          if inputAllTickets == viewingTicketsOptions[1]:
            viewingAllTickets = False
          elif inputAllTickets == viewingTicketsOptions[2]:
            pageCounter += 1
            r = getJsonData(r["links"]["next"])
            continue
          elif inputAllTickets == viewingTicketsOptions[0]:
            pageCounter -= 1
            r = getJsonData(r["links"]["prev"])
            continue
        
        # On the last page of results
        elif pageCounter > 0 and not r['meta']['has_more']:
          inputAllTickets = getInput(allTicketsPrompt4, viewingTicketsOptions[:2])
          if inputAllTickets == viewingTicketsOptions[1]:
            viewingAllTickets = False
          elif inputAllTickets == viewingTicketsOptions[0]:
            pageCounter -= 1
            r = getJsonData(r["links"]["prev"])
            continue

    # View an individual ticket
    elif inputOption == mainOptions[1]:
      viewingIndivTicket = True
      while viewingIndivTicket:
        inputIndivTicket = getInput(individualTicketPrompt1, DIGIT)
        url = f"https://{SUBDOMAIN}.zendesk.com/api/v2/search.json?query={inputIndivTicket}"
        r = getJsonData(url)
        if r['count'] == 0:
          print(individualTicketPrompt2)
          inputIndivTicket = getInput(individualTicketPrompt4, viewingTicketsOptions[:2])
          if inputIndivTicket == viewingTicketsOptions[1]:
            viewingIndivTicket = False
          continue
        else:
          printTickets(r['results'], False)
        inputIndivTicket = getInput(individualTicketPrompt3, viewingTicketsOptions[:2] + [viewingTicketsOptions[3]])
        if inputIndivTicket == viewingTicketsOptions[1]:
          viewingIndivTicket = False
        elif inputIndivTicket == viewingTicketsOptions[3]:
          printDescription(r['results'])
          inputIndivTicket = getInput(individualTicketPrompt4, viewingTicketsOptions[:2])
          if inputIndivTicket == viewingTicketsOptions[1]:
            viewingIndivTicket = False

if __name__ == '__main__':
    main()