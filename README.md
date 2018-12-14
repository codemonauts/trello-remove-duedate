# trello-remove-duedate

When using Trello in a kanban style fashion, you probably have lists with names like Backlog,Doing,Done,Blocked. The problem is that Trello doesn't understands the semantics of these boards and therefore will alert you when a due date is reached even if the card is
already in the 'Done' list. Therefore this tool will look for a 'Done' list in all of your boards and remove the due date from every card in it.
You can run this e.g. as a Lambda function on AWS or as a cronjob on one of your servers.

## Setup

1. Go to [https://trello.com/app-key/](https://trello.com/app-key/) and get yourself a API key and token for Trello
2. Find out the name of your organisation. When you are on the board overview of your organisation check the url which should have the format `https://trello.com/<organisation-name>``
3. Set TRELLO_KEY, TRELLO_TOKEN and ORGANISATION_NAME as environment variables.
4. Make sure you have Python3 and the requests package installed
5. Run it with `python3 main.py` or as a Lambda function with `main.main` as handler