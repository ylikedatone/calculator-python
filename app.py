from flask import Flask

#app variable is a new object that inherits from class Flask (getting all attributes + methods built into the class)
app = Flask(__name__)

#bind fuction to an URL path --> use route method/attribute as decorator
#pass the required route to the decorator
@app.route('/')
def hello():
    greet = '<h1>Hello World!</h1>'
    link = '<p><a href="user/Petunia">This is a test!!!!!!</a></p?' 
    return greet + link

#the name is passed through
@app.route('/user/<name>')
def user(name):
    personal = f'<h1>Hello, {name}! What is your name, {name}?</h1>'
    instruc = '<p>Change the name in the <em>browser address bar</em> \
        and reload the page.</p>'
    return personal + instruc

if __name__ == '__main__':
    app.run(debug=True)
