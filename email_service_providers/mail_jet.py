# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 31/01/22
# -----------------------------------------------

from mailjet_rest import Client
from response_message import ResponseMessage

_data = {
        'Messages': [
            {
                "From": {
                    "Email": "chaudharimohit39@gmail.com",
                    "Name": "Sender"
                },
                "To": [
                    {
                        "Email": "chaudharimohit39@gmail.com",
                        "Name": "Receiver"
                    }
                ],
                "Subject": "Greetings from Mailjet.",
                "TextPart": "My first Mailjet email",
                "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
                "CustomID": "AppGettingStartedTest"
            }
        ]
    }


class MailJet:

    @staticmethod
    def send_mail(mail=None):
        if mail is None:
            return ResponseMessage.FAILURE

        global _data
        _data["Messages"][0]["Subject"] = mail["subject"]
        _data["Messages"][0]["TextPart"] = mail["text"]
        _data["Messages"][0]["From"]["Email"] = mail["from"]
        _data["Messages"][0]["To"][0]["Email"] = mail["to"]

        api_key = '795b9889f0c4aa7f75f3da082909215c'
        api_secret = 'fabb5ba24ffc81c9faaba8748ecdf905'
        mailjet = Client(auth=(api_key, api_secret), version='v3.1')

        result = mailjet.send.create(data=_data)

        if result == 200:
            return ResponseMessage.SUCCESS
        else:
            return ResponseMessage.FAILURE
