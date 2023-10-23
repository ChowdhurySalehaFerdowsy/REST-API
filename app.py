from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # This function defines a route that responds with "Hello, world!"
    return "Hello, World! Nabil is ssweeeeeeeeeeeeeeet "

# In Python, double underscores, such as __name__, have special meanings.
# In this case, __name__ is a built-in variable that represents the name of the current module.


if __name__ == '__main__': # make sure to have a space before and after the  ==
 app.run()

# The condition checks if the script is being run as the main program,
    # and if it is, it will execute app.run()

