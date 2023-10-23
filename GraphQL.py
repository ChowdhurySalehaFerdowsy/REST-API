from flask import Flask, jsonify, request
from flask_graphql import GraphQLView
import graphene

# Define a class for the Stock type
class Stock(graphene.ObjectType):
    name = graphene.String()
    ticker = graphene.String()
    price = graphene.Float()
    historical_prices = graphene.List(graphene.Float)
    highest_price = graphene.Float()
    lowest_price = graphene.Float()
    trading_volume = graphene.Float()


# Define a list of stocks
stocks = [
    {
        "name": "Company A",
        "ticker": "A",
        "price": 100.0,
        "historical_prices": [95.0, 105.0, 110.0, 90.0, 100.0],
        "highest_price": 110.0,
        "lowest_price": 90.0,
        "trading_volume": 1000000.0
    },
    {
        "name": "Company B",
        "ticker": "B",
        "price": 50.0,
        "historical_prices": [45.0, 55.0, 60.0, 40.0, 50.0],
        "highest_price": 60.0,
        "lowest_price": 40.0,
        "trading_volume": 500000.0
    },
    {
        "name": "Company C",
        "ticker": "C",
        "price": 75.0,
        "historical_prices": [70.0, 80.0, 85.0, 65.0, 75.0],
        "highest_price": 85.0,
        "lowest_price": 65.0,
        "trading_volume": 750000.0
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
                    historical_prices=stock['historical_prices'],
                    highest_price=stock['highest_price'],
                    lowest_price=stock['lowest_price'],
                    trading_volume=stock['trading_volume']
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