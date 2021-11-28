import textwrap
from tabulate import tabulate

def getInput(prompt, constraint):
  print(prompt)
  userInput = input()
  if len(constraint) == 1:
    while userInput != constraint:
      print(prompt)
      userInput = input()
  elif constraint == 'digit':
    while not userInput.isdigit():
      print(prompt)
      userInput = input()
  else:
    while userInput not in constraint:
      print(prompt)
      userInput = input()
  return userInput

def printTickets(tickets, allTicketsView):
  formattedTickets = {}
  error = False
  if allTicketsView:
    for ticket in tickets:
      try:
        formattedTickets['ID'] = formattedTickets.get('ID', []) + [ticket['id']]
        formattedTickets['Created At'] = formattedTickets.get('Created At', []) + [ticket['created_at']]
        formattedTickets['Updated At'] = formattedTickets.get('Updated At', []) + [ticket['updated_at']]
        formattedTickets['Priority'] = formattedTickets.get('Priority', []) + [ticket['priority']]
        formattedTickets['Status'] = formattedTickets.get('Status', []) + [ticket['status']]
        formattedTickets['Subject'] = formattedTickets.get('Subject', []) + [ticket['subject']]
      except KeyError:
        error = True
        print("****PROGRAM ERROR: Correct formatted data not received from API call****")
        break
  else:
    try:
      formattedTickets['ID'] = [tickets[0]['id']]
      formattedTickets['Created At'] = [tickets[0]['created_at']]
      formattedTickets['Updated At'] = [tickets[0]['updated_at']]
      formattedTickets['Type'] = [tickets[0]['type']]
      formattedTickets['Priority'] = [tickets[0]['priority']]
      formattedTickets['Status'] = [tickets[0]['status']]
      formattedTickets['Subject'] = [tickets[0]['subject']]
      formattedTickets['Description'] = ['\n'.join(textwrap.wrap(tickets[0]['description'], width=30))]
    except KeyError:
      error = True
      print("****PROGRAM ERROR: Correct formatted data not received from API call****")
      
  if not error:
    print(tabulate(formattedTickets, headers='keys', missingval='N/A'))