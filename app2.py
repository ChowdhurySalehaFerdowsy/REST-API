from flask import Flask, jsonify, request
app = Flask(__name__)

# In Python, double underscores, such as __name__, have special meanings.
# In this case, __name__ is a built-in variable that represents the name of the current module.

#created a list to store the stocks

stocks = []

#Create a route to add new stocks
#Define a new route for adding stock data. For example, 
#you can create an endpoint to add a new stock entry. 
#This is typically done with an HTTP POST request.

# add routes and functionality for stock 
# data entry and retrieval

@app.route('/stock', methods=['POST'])
def add_stock():
   stock = request.get_json()
   stocks.append(stock)
   return jsonify({'message': 'Stock added successfully'})

#Created a route to fetch all stocks:

@app.route('/stocks', methods=['GET'])
def get_stocks():
  return jsonify({'stocks':stocks})
  

if __name__ == '__main__': # make sure to have a space before and after the  ==
 app.run(debug=True)

# The condition checks if the script is being run as the main program,
    # and if it is, it will execute app.run()

