from message import Message
class SMS(Message):
    def __init__(self, message, sender, recipient):
        super().set_message(message)
        self.sender=sender
        self.recipient=recipient

    def send(self):
        print('Sending SMS' + '\n' 'From: ' + self.sender + '\nTo: ' + self.recipient + '\n' +self.message)

class email(Message):
    def __init__(self, message, sender, recipient, subject):
        super().set_message(message)
        self.sender=sender
        self.recipient=recipient
        self.subject=subject
        
    def send(self):
        print('Sending email...' + '\n' 'From: ' + self.sender + '\nTo: ' + self.recipient + '\nSubject: ' + self.subject + '\n' +self.message)
        
    
    


sms1=SMS('hEJ','me','you')
sms1.send()
print()
email1=email('witam pana', 'karolbuldak', 'marekmostowiak', 'jestem fanem')
email1.send()
