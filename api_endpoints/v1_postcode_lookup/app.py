import os

from mangum import Mangum
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from middleware import MIDDLEWARE
from utils import init_sentry
from upstream_api_client import DCApiClient, DevsDCException

client = DCApiClient()

init_sentry()


def get_postcode_response(request: Request):
    postcode = request.path_params["postcode"]
    try:
        response = client.get_postcode_response(request, postcode)
    except DevsDCException as error:
        return JSONResponse(error.message, error.status)
    return JSONResponse(response)


def get_address_response(request: Request):
    uprn = request.path_params["uprn"]
    try:
        response = client.get_uprn_response(request, uprn)
    except DevsDCException as error:
        return JSONResponse(error.message, error.status)
    return JSONResponse(response)


routes = [
    Route(
        "/api/v1/postcode/{postcode}/",
        get_postcode_response,
        methods=["GET"],
        name="postcode",
    ),
    Route(
        "/api/v1/address/{uprn}/",
        get_address_response,
        methods=["GET"],
        name="address",
    ),
]

app = Starlette(
    debug=os.environ.get("DEBUG", False), routes=routes, middleware=MIDDLEWARE
)

handler = Mangum(app, lifespan="off")