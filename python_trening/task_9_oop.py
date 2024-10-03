class Button:

    def __init__(self, text, link):
        self.text = text
        self.link = link

home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

print(home.text)
print('кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)

class Page:
    def __init__(self,url):
        self.url = url

    def get(self):
        print(self.url)
home = Page('kkxkx')
home.get()