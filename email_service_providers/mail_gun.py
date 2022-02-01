# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 31/01/22
# -----------------------------------------------

import requests
from response_message import ResponseMessage


class MailGun:

    @staticmethod
    def send_mail(mail=None):
        if mail is None:
            return ResponseMessage.FAILURE
        response = requests.post(
            "https://api.mailgun.net/v3/sandboxdd1be88ad4da44a284ce3b638d77ba32.mailgun.org/messages",
            auth=("api", "a002edd46b44c1165476cd8023ff26f5-ef80054a-1156fc25"),
            data=mail)

        if response.ok:
            return ResponseMessage.SUCCESS
        else:
            return ResponseMessage.FAILURE
