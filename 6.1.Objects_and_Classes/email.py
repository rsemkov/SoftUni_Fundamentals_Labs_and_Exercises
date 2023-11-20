class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails_list = []
while True:
    command = input()

    if command == "Stop":
        break

    email_sender, email_receiver, email_content = command.split()

    email = Email(email_sender, email_receiver, email_content)

    emails_list.append(email)

indices_to_send = list(map(int, input().split(", ")))

for index, item in enumerate(emails_list):
    if index in indices_to_send:
        item.send()

    print(item.get_info())
