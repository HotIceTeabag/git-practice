from fastapi import FastAPI
from pydantic import BaseModel, Field


class OrderIn(BaseModel):
    price: int = Field(ge=0)
    quantity: int = Field(gt=0)
    
def cerate_app() -> FastAPI:
    app = FastAPI()
    store: dict[int, int] = {}
    
    return app

    @app.post("/orders", status_code=201)
    def create_order(data: OrderIn):
        order_id = len(store) + 1
        store[Order_id] = subtotal(data.price, data.quantity)
        return {"id": order_id, "subtotal": store[order_id]}
    
    @app.get("/orders/{order_id}")
    def get_order(order_id: int):
        if order_id not in store:
            raise HTTPExeption(statue_code=404, detail="Not found")
        return {"id": order_id, "subtotal": store[order_id]}