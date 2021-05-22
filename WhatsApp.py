from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import qrcode
import time
import PySimpleGUI as sg


class WhatsApp:
    chrome_options = Options()
    driver = ""
    name = ""
    img = ""
    test = None

    def __init__(self, name, driverPath):

        self.name = name
        self.chrome_options.add_argument("user-data-dir=Users/" + name)
        self.chrome_options.add_argument("--profile-directory=Default")
        self.chrome_options.add_argument("--remote-debugging-port=9292")
        self.driver = webdriver.Chrome(executable_path=driverPath, options=self.chrome_options)
        self.driver.implicitly_wait(1)

    def login(self, showImg=False):
        self.driver.get('https://web.whatsapp.com')
        data = ""
        while True:
            time.sleep(0.3)
            try:
                code = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div")
                code = code.get_attribute("data-ref")

                if data != code and code is not None:
                    data = code
                    print("#####################################")
                    if showImg == True:
                        self.getQrCodeForImg(code)
                    else:
                        self.getQrCode(code)
                    time.sleep(1)
                    continue
            except:
                try:
                    clicker = self.driver.find_element_by_xpath(
                        '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/div/span/div')
                    clicker.click()
                    print("####ERROR#### PLEASE WAIT")
                    continue
                except:
                    try:
                        data = self.driver.find_element_by_xpath(
                            "/html/body/div[1]/div/div/div[2]/div[1]/div/div[2]/div")
                        data = data.get_attribute("data-ref")
                        continue
                    except:
                        print("Login Succesfully.")

                        return True

    def getQrCode(self, data):
        qr = qrcode.QRCode(
            version=3,
            box_size=1,
            border=0
        )

        qr.add_data(data)
        qr.make(fit=True)
        qr.make_image(fill_color="black", back_color="white")
        qr.print_ascii()

    def getQrCodeForImg(self, data):
        qr = qrcode.QRCode(
            version=5,
            box_size=10,
            border=5
        )

        qr.add_data(data)
        qr.make(fit=True)
        self.img = qr.make_image(fill_color="black", back_color="white")
        self.img.save("test.png")
        sg.Window('My window').Layout([[sg.Image('test.png')]]).Read()

        try:
            print("")
            # self.test.kill()
        except:
            print("ERROR! LOAD NOT QR")

    def send_message(self, number, text):
        print("mesaj gidiyor" + text)
        self.driver.get("https://web.whatsapp.com/send?phone=" + number + "&text=" + text + "&app_absent=0")
        while True:
            time.sleep(0.03)
            try:
                self.driver.find_element_by_class_name("_1E0Oz").click()
                return True
            except:
                continue

    def get_data(self, number):
        self.driver.get("https://web.whatsapp.com/send?phone=" + number + "&text=&app_absent=0")
        while True:
            time.sleep(0.03)
            try:
                clicker = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span')
                break
            except:
                continue
        clicker.click()
        numdatas = self.driver.find_element_by_tag_name("section").text.split("\n")
        return numdatas





