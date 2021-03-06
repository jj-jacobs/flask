from flask import Flask, render_template  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<num_box>')
def lots_box(num_box):
    return render_template('name.html', some_boxes=num_box)

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
