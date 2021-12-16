import time
import smtplib, ssl
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0')

browser = webdriver.Chrome(options = options)
browser.set_page_load_timeout(60)

browser.get('https://direct.playstation.com/en-us/consoles/console/playstation5-console.3006646')
while True:
    all_p = browser.find_elements_by_tag_name("p")
    all_p = [i.text for i in all_p]
    time.sleep(30)

    if "Out of Stock" in all_p:
        print("Item not in stock")
    else:
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"
        sender_email = "INSERT THE EMAIL YOU WANT THE BOT TO SEND FROM HERE"
        receiver_email = "INSERT THE EMAIL YOU WANT THE BOT TO SEND TO HERE"
        password = "INSERT THE PASSWORD OF THE EMAIL THE BOT IS SENDING FROM HERE"
        message = """\
        Subject: PS5 Restock Detected
    
        Commence Trolling"""

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            print("Item in Stock")

browser.close()
