from flask import Flask, jsonify, request

from flask_graphql import GraphQLView 

#GraphQLView is part of the Flask-GraphQL library and 
# is used to add a GraphQL route to your Flask application
import graphene #  Graphene is a Python library that is used to define and work with 
#GraphQL schemas, types, and resolvers. 
# It provides the necessary building blocks for creating a 
# GraphQL API in Python

app = Flask(__name__)

# In Python, double underscores, such as __name__, have special meanings.
# In this case, __name__ is a built-in variable that represents the name of the current module.

#define a GraphQL Schema usng graphene
class Stock(graphene.ObjectType):
  name=graphene.String()
  ticker_symbol= graphene.String()
  current_price= graphene.Float()

class Query(graphene.ObjectType):
  stocks = graphene.List(Stock)

def resolve_stocks(self, info):
  return stocks

schema=graphene.Schema(query=Query)


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

