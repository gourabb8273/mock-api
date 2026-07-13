from fastapi import FastAPI, Header, HTTPException

app = FastAPI(title="Car Model API")

API_TOKEN = "xyz12349dhwnsjasjojqoaj"
# https://mock-api-wet8.onrender.com
# GET /get-car-model-data                -> Raw array
# GET /get-car-model-data-data           -> { "data": [...] }
# GET /get-car-model-data-items          -> { "items": [...] }
# GET /get-car-model-data-nested         -> { "data": { "items": [...], "total": 10 } }

# GET /get-dealer-data                   -> Raw array
# GET /get-dealer-data-data              -> { "data": [...] }
# GET /get-dealer-data-items             -> { "items": [...] }
# GET /get-dealer-data-nested            -> { "data": { "items": [...], "total": 5 } }
# ----------------------------
# Sample Data
# ----------------------------

# ============================================================
# Car Variant APIs
# ============================================================
# GET /get-car-variant-data              -> Raw array
# GET /get-car-variant-data-data         -> { "data": [...] }
# GET /get-car-variant-data-items        -> { "items": [...] }
# GET /get-car-variant-data-nested       -> { "data": { "items": [...], "total": 10 } }

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

CAR_VARIANTS = [
    {
        "car_variant_id": "CV001",
        "car_model_id": "CM001",
        "car_variant": "Sedan LX MT",
        "fuel_type": "Petrol",
        "transmission_type_id": "MT",
        "upsellingEnabled": "true",
        "exShowroomPrice": "850000"
    },
    {
        "car_variant_id": "CV002",
        "car_model_id": "CM001",
        "car_variant": "Sedan LX AT",
        "fuel_type": "Petrol",
        "transmission_type_id": "AT",
        "upsellingEnabled": "true",
        "exShowroomPrice": "920000"
    },
    {
        "car_variant_id": "CV003",
        "car_model_id": "CM002",
        "car_variant": "SUV X5 Diesel MT",
        "fuel_type": "Diesel",
        "transmission_type_id": "MT",
        "upsellingEnabled": "false",
        "exShowroomPrice": "1450000"
    },
    {
        "car_variant_id": "CV004",
        "car_model_id": "CM002",
        "car_variant": "SUV X5 Diesel AT",
        "fuel_type": "Diesel",
        "transmission_type_id": "AT",
        "upsellingEnabled": "true",
        "exShowroomPrice": "1580000"
    },
    {
        "car_variant_id": "CV005",
        "car_model_id": "CM003",
        "car_variant": "Hatchback S MT",
        "fuel_type": "Petrol",
        "transmission_type_id": "MT",
        "upsellingEnabled": "true",
        "exShowroomPrice": "690000"
    },
    {
        "car_variant_id": "CV006",
        "car_model_id": "CM004",
        "car_variant": "Coupe GT Turbo",
        "fuel_type": "Petrol",
        "transmission_type_id": "AT",
        "upsellingEnabled": "false",
        "exShowroomPrice": "2100000"
    },
    {
        "car_variant_id": "CV007",
        "car_model_id": "CM005",
        "car_variant": "Pickup XL 4x2",
        "fuel_type": "Diesel",
        "transmission_type_id": "MT",
        "upsellingEnabled": "true",
        "exShowroomPrice": "1320000"
    },
    {
        "car_variant_id": "CV008",
        "car_model_id": "CM006",
        "car_variant": "Electric E1 Long Range",
        "fuel_type": "Electric",
        "transmission_type_id": "AT",
        "upsellingEnabled": "true",
        "exShowroomPrice": "1690000"
    },
    {
        "car_variant_id": "CV009",
        "car_model_id": "CM007",
        "car_variant": "Hybrid H7 Premium",
        "fuel_type": "Hybrid",
        "transmission_type_id": "AT",
        "upsellingEnabled": "true",
        "exShowroomPrice": "1880000"
    },
    {
        "car_variant_id": "CV010",
        "car_model_id": "CM010",
        "car_variant": "Mini M3 Standard",
        "fuel_type": "Petrol",
        "transmission_type_id": "MT",
        "upsellingEnabled": "false",
        "exShowroomPrice": "620000"
    }
]

DEALERS = [
    {
        "dealer_id": "DL001",
        "dealer_name": "Acme Arena Kolkata",
        "dealer_code": "AR001",
        "full_address": "Salt Lake Sector V, Kolkata",
        "lat": 22.5726,
        "long": 88.3639,
        "distance": "2.4 km",
        "channel": "Arena"
    },
    {
        "dealer_id": "DL002",
        "dealer_name": "Acme Nexa Park Street",
        "dealer_code": "NX001",
        "full_address": "Park Street, Kolkata",
        "lat": 22.5548,
        "long": 88.3507,
        "distance": "4.8 km",
        "channel": "NEXA"
    },
    {
        "dealer_id": "DL003",
        "dealer_name": "Acme Arena Howrah",
        "dealer_code": "AR002",
        "full_address": "Howrah Maidan",
        "lat": 22.5958,
        "long": 88.2636,
        "distance": "8.5 km",
        "channel": "Arena"
    },
    {
        "dealer_id": "DL004",
        "dealer_name": "Acme Nexa New Town",
        "dealer_code": "NX002",
        "full_address": "New Town, Kolkata",
        "lat": 22.5867,
        "long": 88.4789,
        "distance": "6.2 km",
        "channel": "NEXA"
    },
    {
        "dealer_id": "DL005",
        "dealer_name": "Acme Arena Garia",
        "dealer_code": "AR003",
        "full_address": "Garia, Kolkata",
        "lat": 22.4593,
        "long": 88.3850,
        "distance": "12.7 km",
        "channel": "Arena"
    }
]


# ----------------------------
# Helpers
# ----------------------------

def authenticate(authorization: str):
    if authorization != f"Bearer {API_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")


def raw(data):
    return data


def data_wrapper(data):
    return {
        "data": data
    }


def items_wrapper(data):
    return {
        "items": data
    }


def nested_wrapper(data):
    return {
        "data": {
            "items": data,
            "total": len(data)
        }
    }


# ----------------------------
# Health
# ----------------------------

@app.get("/")
def health():
    return {"status": "running"}


# ============================================================
# Car Model Endpoints
# ============================================================

# Raw Array
@app.get("/get-car-model-data")
def get_car_models_raw(authorization: str = Header(None)):
    authenticate(authorization)
    return raw(CAR_MODELS)


# { "data": [...] }
@app.get("/get-car-model-data-data")
def get_car_models_data(authorization: str = Header(None)):
    authenticate(authorization)
    return data_wrapper(CAR_MODELS)


# { "items": [...] }
@app.get("/get-car-model-data-items")
def get_car_models_items(authorization: str = Header(None)):
    authenticate(authorization)
    return items_wrapper(CAR_MODELS)


# { "data": { "items": [...], "total": n } }
@app.get("/get-car-model-data-nested")
def get_car_models_nested(authorization: str = Header(None)):
    authenticate(authorization)
    return nested_wrapper(CAR_MODELS)


# ============================================================
# Dealer Endpoints
# ============================================================

# Raw Array
@app.get("/get-dealer-data")
def get_dealers_raw(authorization: str = Header(None)):
    authenticate(authorization)
    return raw(DEALERS)


# { "data": [...] }
@app.get("/get-dealer-data-data")
def get_dealers_data(authorization: str = Header(None)):
    authenticate(authorization)
    return data_wrapper(DEALERS)


# { "items": [...] }
@app.get("/get-dealer-data-items")
def get_dealers_items(authorization: str = Header(None)):
    authenticate(authorization)
    return items_wrapper(DEALERS)


# { "data": { "items": [...], "total": n } }
@app.get("/get-dealer-data-nested")
def get_dealers_nested(authorization: str = Header(None)):
    authenticate(authorization)
    return nested_wrapper(DEALERS)


# ============================================================
# Car Variant Endpoints
# ============================================================

# Raw Array
@app.get("/get-car-variant-data")
def get_car_variants_raw(authorization: str = Header(None)):
    authenticate(authorization)
    return raw(CAR_VARIANTS)


# { "data": [...] }
@app.get("/get-car-variant-data-data")
def get_car_variants_data(authorization: str = Header(None)):
    authenticate(authorization)
    return data_wrapper(CAR_VARIANTS)


# { "items": [...] }
@app.get("/get-car-variant-data-items")
def get_car_variants_items(authorization: str = Header(None)):
    authenticate(authorization)
    return items_wrapper(CAR_VARIANTS)


# { "data": { "items": [...], "total": n } }
@app.get("/get-car-variant-data-nested")
def get_car_variants_nested(authorization: str = Header(None)):
    authenticate(authorization)
    return nested_wrapper(CAR_VARIANTS)