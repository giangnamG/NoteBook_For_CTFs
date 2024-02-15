from flask import Flask, request, render_template
import xml.sax

app = Flask(__name__)

class BookHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        # if name == "book":
            print("Start element:", name)
            # print("attrs:", attrs.get('id'))
            pass

    def endElement(self, name):
        # print("End element:", name)
        pass
    def characters(self, content):
        print("Character data:", content)

class BookXML():
    def __init__(self):
        self.parser = xml.sax.make_parser()
        self.handler = BookHandler()
        self.parser.setContentHandler(self.handler)

    def prepareXML(self):
        with open('./book.xml', 'rb') as f:
            file_contents = f.read()
            self.parser.feed(file_contents)

books = BookXML()
books.prepareXML()

@app.route('/',methods=['GET','POST'])

def index():
    if request.method == 'GET':
        return render_template('index.html')
    
# if __name__ == '__main__':
#     app.run(debug=True)