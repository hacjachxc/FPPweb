from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World!'
 
if __name__ == '__main__':
    app.run(debug=True)
    print("test02")
    print("test03")
    print("test04")
    print("test05")