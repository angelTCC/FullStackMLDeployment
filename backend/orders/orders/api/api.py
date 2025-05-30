import uuid
from datetime import datetime
from uuid import UUID

from http import HTTPStatus
from fastapi import HTTPException
from starlette import status
from starlette.responses import Response

from orders.app import app


order = {
    'id': 'ff0f1355-e821-4178-9567-550dec27a373',
    'status': "delivered",
    'created': datetime.now(),
    'order': [
        {
        'product': 'cappuccino',
        'size': 'medium',
        'quantity': 1
        }
    ]
}

@app.get('/orders')
def get_orders():
    return {'orders': [order] }

@app.post('/orders', status_code=status.HTTP_201_CREATED)
def create_order():
    return order

@app.get('/orders/{order_id}')
def get_order(order_id: UUID):
    return order

@app.put('/orders/{order_id}')
def update_order(order_id: UUID):
    return order

@app.delete('/orders/{order_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: UUID):
    return Response(status_code=HTTPStatus.NO_CONTENT.value)

@app.post('/orders/{order_id}/cancel')
def cancel_order(order_id: UUID):
    return order

@app.post('/orders/{order_id}/pay')
def pay_order(order_id: UUID):
    return order