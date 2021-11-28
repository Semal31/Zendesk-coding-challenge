# Zendesk Coding Challenge -- CLI Approach
Take home coding assesment building a ticket viewer with the Zendesk API

## Setup
1. Install requirements (depending on your setup use `pip` instead of `pip3`):
```shell
$ pip3 install -r requirements.txt
```
2. .env file:
- An `.env_template` file is provided. Remove the `_template` from the filename and replace the `{email}`, `{token}`, and `{subdomain}` fields with your respective email, API token, and subdomain (ex: `zcc2973`)

## Usage
1. Start the program (depending on your setup use `python` instead of `python3`) **Python 3 is needed**:
```shell
$ python3 main.py
```
- **NOTE:** When running the program if the format of the table does not look right or match the format below you will need the shell wider
  - There is an issue where the text will not wrap correctly if the shell window length is not wide enough 
2. If the program connected to the API correctly you should get the welcome message:
```
Welcome to the ticket viewer V1
The options are as follows:
    'a' to view all tickets
    'i' to select an individual ticket to view 
    'q' to quit the application
```
- If `Cannot establish a connection to the API...` is printed then either your credentials are incorrect or the API is unavailable 
- Individual tickets are selected by id
3. Format of viewing all tickets:
```
  ID  Created At            Updated At            Priority    Status    Subject
----  --------------------  --------------------  ----------  --------  ---------------------------------------------
   1  2021-11-26T18:24:43Z  2021-11-26T18:24:43Z  normal      open      Sample ticket: Meet the ticket
```
4. Format of viewing an individual ticket:
```
  ID  Created At            Updated At            Type      Priority    Status    Subject
----  --------------------  --------------------  --------  ----------  --------  ------------------------------
   1  2021-11-26T18:24:43Z  2021-11-26T18:24:43Z  incident  normal      open      Sample ticket: Meet the ticket
```
- then you may input 'd' to view the description

## Testing
1. Automated testing is done through Github Actions:
- The tests are done on each push to Github and can be viewed in the `Action` tab of the repository
2. Use Pytest manually:
```shell
$ pytest
```
run the command above in the root folder of the repository to run all tests
