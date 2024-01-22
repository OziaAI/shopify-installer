from flask import request, abort, redirect
import shopify
import binascii
import os

from ..tools import check_hmac


def install_route():
    args = request.args
    if not args["hmac"]:
        abort(code=400)

    session = shopify.Session(args["shop"], "2024-01")
    access_token = session.request_token(args)



