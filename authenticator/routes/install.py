from flask import request, abort, redirect
import shopify
import binascii
import os

from ..tools import check_hmac


def install_route():
    args = request.args
    if not args["hmac"]:
        abort(code=400)

    match = check_hmac(args)

    if not match:
        return abort(code=401)

    session = shopify.Session(args["shop"], "2024-01")
    redirect_url = "https://ozia.ai"
    state = binascii.b2a_hex(os.urandom(15)).decode("utf-8")
    scopes = ["read_products", "read_orders"]

    auth_url = session.create_permission_url(scopes, redirect_url, state)

    return redirect(auth_url, code=302)
