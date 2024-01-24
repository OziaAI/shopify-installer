from flask import request, abort, redirect
import shopify

from ..tools import get_db


def exchange_token():
    args = request.args
    if not args["hmac"]:
        abort(code=400)

    session = shopify.Session(args["shop"], "2024-01")
    access_token = session.request_token(args)
    
    db = get_db()
    cur = db.cursor()

    cur.execute("INSERT INTO access (token, shop)"
                "VALUES (%s, %s)",
                (access_token,
                 args["shop"])
                )

    redirect("https://login.ozia.ai")


