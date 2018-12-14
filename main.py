#! /usr/bin/env python3
import os

try:
    import requests
except ImportError:
    # Take requests from boto if run with AWS Lambda
    from botocore.vendored import requests

KEY = os.environ.get('TRELLO_KEY', None)
TOKEN = os.environ.get('TRELLO_TOKEN', None)
ORGANISATION = os.environ.get('ORGANISATION_NAME', None)


def get_boards(organisation):
    r = requests.get("https://api.trello.com/1/organizations/{}/boards".format(organisation),
                     params={"key": KEY, "token": TOKEN})
    if r.status_code == 200:
        return r.json()
    else:
        print("Couldn't load boards. Error was:")
        print(r)


def get_lists(board_id):
    r = requests.get("https://api.trello.com/1/boards/{}/lists".format(board_id),
                     params={"key": KEY, "token": TOKEN})
    if r.status_code == 200:
        return r.json()
    else:
        print("Couldn't load lists for this board. Error was:")
        print(r)


def get_cards(done_id):
    r = requests.get("https://api.trello.com/1/lists/{}/cards".format(done_id),
                     params={"key": KEY, "token": TOKEN})
    if r.status_code == 200:
        return r.json()
    else:
        print("Couldn't load cards for this list. Error was:")
        print(r)


def remove_due_date(card_id):
    r = requests.put("https://api.trello.com/1/cards/{}/due?value=null".format(card_id),
                     params={"key": KEY, "token": TOKEN})
    if r.status_code == 200:
        return r.json()
    else:
        print("Couldn't remove due date from card. Error was:")
        print(r)


def main(event=None, context=None):
    boards = get_boards(organisation=ORGANISATION)
    for board in boards:
        id = board["id"]
        name = board["name"]
        print("Processing {}...".format(name))
        lists = get_lists(board_id=id)
        for l in lists:
            if l["name"] == "Done":
                done_id = l["id"]

        if not done_id:
            print("Found no 'Done' list")
            continue

        cards = get_cards(done_id=done_id)
        for c in cards:
            if c["due"]:
                card_id = c["id"]
                card_title = c["name"]
                print("Removing due date from '{}'".format(card_title))
                remove_due_date(card_id)


if __name__ == "__main__":
    main()
