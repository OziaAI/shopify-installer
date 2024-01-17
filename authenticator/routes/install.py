from flask import request, abort, redirect
from ..tools import check_hmac

def install_route():
    # scopes = ["read_products", "read_orders"]

    args = request.args
    if not args["hmac"]:
        abort(code=400)

    match = check_hmac(args)

    if not match:
        return abort(code=401)

    redirect_url = "https://ozia.ai"
    return redirect(redirect_url, code=302)


