#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<int:id>')
def contract(id):
    match = next((contract for contract in contracts if contract["id"] == id), None)
    if match:
        status_code = 200
        headers = {}
        return make_response(match["contract_information"], status_code, headers)
    
    response_body = f"Contract with ID:{id} not found"
    status_code = 404
    headers = {}
    return make_response(response_body, status_code, headers)

@app.route('/customer/<string:customer_name>')
def customer(customer_name):
    if customer_name in customers:
        response_body = ""
        status_code = 204
        headers = {}
        return make_response(response_body, status_code, headers)
    
    response_body = f"Customer {customer_name} not found"
    status_code = 404
    headers = {}
    return make_response(response_body, status_code, headers)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
