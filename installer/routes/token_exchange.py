from flask import request, abort, redirect
import shopify

from ..tools import get_db, cache, logger


def exchange_token():
    args = request.args
    if not args["hmac"] or not args["state"] or not args["shop"]:
        logger.info("Request is missing crucial parameters")
        abort(code=400)

    state = args["state"]
    state_key = "state:" + args["shop"]
    cached_state = cache.get(state_key)

    if str(state) != str(cached_state):
        logger.info("Request does not have the same state as cached:")
        logger.info("state_key: " + state_key)
        logger.info("cached_state: " + str(cached_state))
        logger.info("given_state: " + state)
        abort(code=401)

    session = shopify.Session(args["shop"], "2024-01")
    access_token = session.request_token(args)

    db = get_db()
    with db.cursor() as cur:
        cur.execute(
            "INSERT INTO shopify_access (access_token, shop)" "VALUES (%s, %s)",
            (access_token, args["shop"]),
        )
        db.commit()

    return redirect("https://ozia.ai")
