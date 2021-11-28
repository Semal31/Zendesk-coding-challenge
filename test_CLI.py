from helper import getInput, printDescription, printTickets

# wanted to put all helper tests in their own class but setattr would not work in the class
def test_getInput_charArray_correct(monkeypatch):
  monkeypatch.setattr('builtins.input', lambda: "a")
  assert getInput("example prompt", ['a', 'b']) == 'a'

def test_getInput_char_correct(monkeypatch):
  monkeypatch.setattr('builtins.input', lambda: "a")
  assert getInput("example prompt", 'a') == 'a'

def test_getInput_char_incorrect(monkeypatch):
  monkeypatch.setattr('builtins.input', lambda: "a")
  assert getInput("example prompt", 'a') != 'b'

def test_getInput_charArray_incorrect(monkeypatch):
  monkeypatch.setattr('builtins.input', lambda: "a")
  assert getInput("example prompt", ['a', 'b']) != 'c'

def test_printTickets_allTicketsView_correct(capsys):
  tickets = [
    {
      "id": 1,
      "created_at": "2021-11-26T18:24:43Z",
      "updated_at": "2021-11-26T18:24:43Z",
      "type": "incident",
      "subject": "Sample ticket: Meet the ticket",
      "priority": "normal",
      "status": "open"
    },
    {
      "id": 2,
      "created_at": "2021-11-26T18:41:26Z",
      "updated_at": "2021-11-26T18:41:26Z",
      "type": None,
      "subject": "velit eiusmod reprehenderit officia cupidatat",
      "priority": None,
      "status": "open"
    },
    {
      "id": 3,
      "created_at": "2021-11-26T18:41:26Z",
      "updated_at": "2021-11-26T18:41:26Z",
      "type": None,
      "subject": "excepteur laborum ex occaecat Lorem",
      "priority": None,
      "status": "open"
    }
  ]
  textFile = open("Test_Files/allTicketsView_test.txt", "r")
  expected = textFile.read()
  printTickets(tickets, True)
  captured = capsys.readouterr()
  assert captured.out == expected

def test_printTickets_indivTicketsView_correct(capsys):
  ticket = [
    {
      "id": 2,
      "created_at": "2021-11-26T18:41:26Z",
      "updated_at": "2021-11-26T18:41:26Z",
      "type": None,
      "subject": "velit eiusmod reprehenderit officia cupidatat",
      "priority": None,
      "status": "open",
      "has_incidents": False,
      "due_at": None,
    }
  ]
  textFile = open("Test_Files/indivTicketView_test.txt", "r")
  expected = textFile.read()
  printTickets(ticket, False)
  captured = capsys.readouterr()
  assert captured.out == expected

def test_printTickets_indivTicketsView_incorrect(capsys):
  # missing the status field
  ticket = [
    {
      "id": 2,
      "created_at": "2021-11-26T18:41:26Z",
      "updated_at": "2021-11-26T18:41:26Z",
      "type": None,
      "subject": "velit eiusmod reprehenderit officia cupidatat",
      "priority": None
    }
  ]
  printTickets(ticket, False)
  captured = capsys.readouterr()
  assert captured.out == "****PROGRAM ERROR: Correct formatted data not received from API call****\n"

def test_printTickets_allTicketsView_incorrect(capsys):
  # missing the updated_at field in ticket 2
  tickets = [
    {
      "id": 1,
      "created_at": "2021-11-26T18:24:43Z",
      "updated_at": "2021-11-26T18:24:43Z",
      "type": "incident",
      "subject": "Sample ticket: Meet the ticket",
      "priority": "normal",
      "status": "open"
    },
    {
      "id": 2,
      "created_at": "2021-11-26T18:41:26Z",
      "type": None,
      "subject": "velit eiusmod reprehenderit officia cupidatat",
      "priority": None,
      "status": "open"
    },
    {
      "id": 3,
      "created_at": "2021-11-26T18:41:26Z",
      "updated_at": "2021-11-26T18:41:26Z",
      "type": None,
      "subject": "excepteur laborum ex occaecat Lorem",
      "priority": None
    }
  ]
  printTickets(tickets, True)
  captured = capsys.readouterr()
  assert captured.out == "****PROGRAM ERROR: Correct formatted data not received from API call****\n"

def test_printDescription_correct(capsys):
  ticket = [
    {
      "id": 2,
      "created_at": "2021-11-26T18:41:26Z",
      "updated_at": "2021-11-26T18:41:26Z",
      "type": None,
      "subject": "velit eiusmod reprehenderit officia cupidatat",
      "description": "Aute ex sunt culpa ex ea esse sint cupidatat aliqua ex consequat sit reprehenderit. Velit labore proident quis culpa ad duis adipisicing laboris voluptate velit incididunt minim consequat nulla. Laboris adipisicing reprehenderit minim tempor officia ullamco occaecat ut laborum.\n\nAliquip velit adipisicing exercitation irure aliqua qui. Commodo eu laborum cillum nostrud eu. Mollit duis qui non ea deserunt est est et officia ut excepteur Lorem pariatur deserunt.",
      "priority": None,
      "status": "open"
    }
  ]
  textFile = open("Test_Files/printDescription_test.txt", "r")
  expected = textFile.read()
  printDescription(ticket)
  captured = capsys.readouterr()
  assert captured.out == expected

def test_printDescription_incorrect(capsys):
  # missing the description field
  ticket = [
    {
      "id": 2,
      "created_at": "2021-11-26T18:41:26Z",
      "updated_at": "2021-11-26T18:41:26Z",
      "type": None,
      "subject": "velit eiusmod reprehenderit officia cupidatat",
      "priority": None
    }
  ]
  printDescription(ticket)
  captured = capsys.readouterr()
  assert captured.out == "****PROGRAM ERROR: Correct formatted data not received from API call****\n"