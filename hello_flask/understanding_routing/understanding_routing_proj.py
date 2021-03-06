from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello():
    print("hello world")
    return render_template('Index.html', phrase="hello", times=5)

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/hello/<name>')
def hello_boy(name):
    print(name)
    return "Hello, " + name

@app.route('/repeat/<number>/<varchar>')
def say_things(number, varchar):
    return varchar * int(number)
        
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.