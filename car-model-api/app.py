from fastapi import FastAPI, Header, HTTPException

app = FastAPI(title="Car Model API")

API_TOKEN = "xyz12349dhwnsjasjojqoaj"

CAR_MODELS = [
    {
        "car_model_id": "CM001",
        "acme_code": "ACM-1001",
        "car_model": "Sedan LX",
        "registration_type": "Private",
        "registration_type_1": "Individual"
    },
    {
        "car_model_id": "CM002",
        "acme_code": "ACM-1002",
        "car_model": "SUV X5",
        "registration_type": "Commercial",
        "registration_type_1": "Fleet"
    },
    {
        "car_model_id": "CM003",
        "acme_code": "ACM-1003",
        "car_model": "Hatchback S",
        "registration_type": "Private",
        "registration_type_1": "Individual"
    },
    {
        "car_model_id": "CM004",
        "acme_code": "ACM-1004",
        "car_model": "Coupe GT",
        "registration_type": "Private",
        "registration_type_1": "Corporate"
    },
    {
        "car_model_id": "CM005",
        "acme_code": "ACM-1005",
        "car_model": "Pickup XL",
        "registration_type": "Commercial",
        "registration_type_1": "Fleet"
    },
    {
        "car_model_id": "CM006",
        "acme_code": "ACM-1006",
        "car_model": "Electric E1",
        "registration_type": "Private",
        "registration_type_1": "Individual"
    },
    {
        "car_model_id": "CM007",
        "acme_code": "ACM-1007",
        "car_model": "Hybrid H7",
        "registration_type": "Government",
        "registration_type_1": "Department"
    },
    {
        "car_model_id": "CM008",
        "acme_code": "ACM-1008",
        "car_model": "Luxury L9",
        "registration_type": "Private",
        "registration_type_1": "Corporate"
    },
    {
        "car_model_id": "CM009",
        "acme_code": "ACM-1009",
        "car_model": "Van V2",
        "registration_type": "Commercial",
        "registration_type_1": "Logistics"
    },
    {
        "car_model_id": "CM010",
        "acme_code": "ACM-1010",
        "car_model": "Mini M3",
        "registration_type": "Private",
        "registration_type_1": "Individual"
    }
]


@app.get("/")
def health():
    return {"status": "running"}


@app.get("/get-car-model-data")
def get_car_model_data(authorization: str = Header(None)):
    if authorization != f"Bearer {API_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {
        "success": True,
        "count": len(CAR_MODELS),
        "data": CAR_MODELS
    }