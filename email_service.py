# -----------------------------------------------
# Author        : Mohit Chaudhari 
# Created Date  : 22/01/22
# -----------------------------------------------

import re

from collections import defaultdict

from email_service_providers.mail_jet import MailJet
from response_message import ResponseMessage
from email_service_providers.mail_gun import MailGun
from email_service_providers.send_grid import SendGrid


class EmailService:

    def __init__(self):
        self._sender_name = None
        self._receiver_name = None
        self._title = None
        self._text = None
        self._cc = None
        self._bcc = None
        self._mail_object = defaultdict()

    @staticmethod
    def _validate_email_address(email_address):
        """
        This is a helper method to validate the email address format
        return True if it is good.
        """
        return bool(re.match(r"[a-zA-Z0-9]+(\.?[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(\.?[a-zA-Z0-9]+)*\.[a-zA-Z0-9]{2,}", email_address))

    def send_email(self, sender=None, receiver=None, cc=None, bcc=None, title=None, text=None):
        """

        :param sender: Senders email address
        :param receiver: Receivers email address
        :param cc: carbon copy
        :param bcc: Blind carbon copy
        :param title: Subject of the email
        :param text: Message to send
        :return: Success or Failure
        """

        # METADATA REQUIRED TO SENT MAIL
        is_sender_valid = self._validate_email_address(sender)
        is_receiver_valid = self._validate_email_address(receiver)

        if cc is not None and self._validate_email_address(cc):
            self._mail_object["cc"] = cc
        if bcc is not None and self._validate_email_address(bcc):
            self._mail_object["bcc"] = bcc

        if is_sender_valid and is_receiver_valid and title is not None and text is not None:

            self._mail_object["from"] = sender
            self._mail_object["to"] = receiver
            self._mail_object["subject"] = title
            self._mail_object["text"] = text

            mail_gun = MailGun()
            mail_jet = MailJet()
            if mail_jet.send_mail(self._mail_object) == ResponseMessage.SUCCESS:
                return ResponseMessage.SUCCESS
            elif mail_gun.send_mail(self._mail_object) == ResponseMessage.SUCCESS:
                return ResponseMessage.SUCCESS
            else:
                return ResponseMessage.FAILURE

        else:
            return ResponseMessage.FAILURE
