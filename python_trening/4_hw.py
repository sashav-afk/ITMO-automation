class Pramoug:
    def __init__(self,h,w):
        self.h = h
        self.w = w
    def square(self):
        print(self.h * self.w)
    def per(self):
        print((self.h + self.w) * 2)

pr1 = Pramoug(2,3)
pr2 = Pramoug(6,5)
pr3 = Pramoug(8,9)
pr1.square()
pr1.per()
pr2.square()
pr2.per()
pr3.square()
pr3.per()

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        print(self.a + self.b)
    def multiplication(self):
        print(self.a * self.b)
    def division(self):
        print(self.a / self.b)
    def subtraction(self):
        print(self.a - self.b)

m1 = Math(6, 7)
m1.addition()
m1.multiplication()
m1.division()
m1.subtraction()

class Button:
    def __init__(self, text, typ, lok=None):
        self.text = text
        self.typ = typ
        self.lok = lok
    def click(self):
        print ("Клик по кнопке", self.text)

Text_box = Button("Text box", "button")
print(Text_box.text)
Text_box.click()
Check_box = Button("Check box", "button")
print(Check_box.text)
Check_box.click()
Radio_button = Button("Radio button", "button")
print(Radio_button.text)
Radio_button.click()
Web_tables = Button("Web tables", "button")
print(Web_tables.text)
Web_tables.click()
Buttons = Button("Buttons", "button")
print(Buttons.text)
Buttons.click()
Links = Button("Links", "button")
print(Links.text)
Links.click()
Broken_link_images = Button("Broken link - images", "button")
print(Broken_link_images.text)
Broken_link_images.click()
Upload_and_download = Button("Upload and download", "button")
print(Upload_and_download.text)
Upload_and_download.click()
Dynamic_properties = Button("Dynamic properties", "button")
print(Dynamic_properties.text)
Dynamic_properties.click()