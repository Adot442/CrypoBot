import yagmail
import time

class Email: 
    def __init__(self):
        self.yag = self.connectAccount()

    def connectAccount(self):
        fp = open("./secret/gmail.txt")
        email = fp.readline()
        password = fp.readline()
        fp.close()
        
        yag = yagmail.SMTP(email, password)
        return yag

    def sendEmail(self, subject, contents):
        contents = [
            "The most recent bitcoin price is:",
            str(contents), "\nGet money,",
            "Cryptobot"
        ]

        try:
            fp = open("./secret/recipients.txt")
        except:
            print("Failed to open recipient file")
            pass


        user = fp.readline()
        line = user
        while(line != ""):
            try:
                self.yag.send(line, subject, contents)
                line = fp.readline()
                print("Sent email!")
            except:
                self.yag.send(user, subject, ["failed sending email"])
                print("failed sending email")
                print(line)
                print(subject)
                print(contents)
                time.sleep(5)


if __name__ == "__main__":
    email = Email()
    email.sendEmail()