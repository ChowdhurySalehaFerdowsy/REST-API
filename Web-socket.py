from flask import Flask, jsonify, request
from flask_graphql import GraphQLView
import graphene
from flask_socketio import SocketIO,emit
#In Flask-SocketIO, emit is a function that is used 
# to send real-time messages or events from the server 
# to connected clients through WebSocket connections. 
# It's essentially a way for the server to "emit" events
#  or messages to the connected clients. This is a common 
# pattern in WebSocket-based applications to enable 
# real-time communication.

socketio= SocketIO(app)

@socketio.on('update_stock_price')
def handle_stock_price_update(data):
    # Handle the stock price update and broadcast it
    emit('stock_price_updated', data, broadcast=True)

# When stock price changes, call the WebSocket event to update clients
socketio.emit('stock_price_updated', updated_data, broadcast=True)


# Define a class for the Stock type
class Stock(graphene.ObjectType):
    name = graphene.String()
    ticker = graphene.String()
    price = graphene.Float()
    historicalPrices = graphene.List(graphene.Float)
    highestPrice = graphene.Float()
    lowestPrice = graphene.Float()
    tradingVolume = graphene.Float()


# Define a list of stocks
stocks = [
    {
        "name": "Company A",
        "ticker": "A",
        "price": 100.0,
        "historicalPrices": [95.0, 105.0, 110.0, 90.0, 100.0],
        "highestPrice": 110.0,
        "lowestPrice": 90.0,
        "tradingVolume": 1000000.0
    },
    {
        "name": "Company B",
        "ticker": "B",
        "price": 50.0,
        "historicalPrices": [45.0, 55.0, 60.0, 40.0, 50.0],
        "highestPrice": 60.0,
        "lowestPrice": 40.0,
        "tradingVolume": 500000.0
    },
    {
        "name": "Company C",
        "ticker": "C",
        "price": 75.0,
        "historicalPrices": [70.0, 80.0, 85.0, 65.0, 75.0],
        "highestPrice": 85.0,
        "lowestPrice": 65.0,
        "tradingVolume": 750000.0
    }
]

# Define a query for fetching a single stock by ticker
class Query(graphene.ObjectType):
    stock = graphene.Field(Stock, ticker=graphene.String(required=True))

    def resolve_stock(self, info, ticker):
        for stock in stocks:
            if stock['ticker'] == ticker:
                return Stock(
                    name=stock['name'],
                    ticker=stock['ticker'],
                    price=stock['price'],
                    historicalPrices=stock['historicalPrices'],
                    highestPrice=stock['highestPrice'],
                    lowestPrice=stock['lowestPrice'],
                    tradingVolume=stock['tradingVolume']
                )
        return None

# Define a schema for the GraphQL API
schema = graphene.Schema(query=Query)

# Create a Flask application
app = Flask(__name__)

# Define a GraphQL view function
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)