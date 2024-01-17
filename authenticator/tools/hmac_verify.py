from ..env import API_SECRET

import json
import hmac
import hashlib


def encode_query_pairs(params):
    """
    Sort and combine query parameters into a single string,
    excluding those that should be removed and joining with '&'.
    """

    def encoded_pairs(params):
        for k, v in params.items():
            if k == 'hmac':
                continue

            if k.endswith('[]'):
                v = json.dumps(params.getlist(k))
                k = k.rstrip('[]')

            # escape delimiters to avoid tampering
            k = str(k).replace("%", "%25").replace("=", "%3D")
            v = str(v).replace("%", "%25")
            yield '{0}={1}'.format(k, v).replace("&", "%26")

    return "&".join(sorted(encoded_pairs(params)))


def check_hmac(params):
    """
    Compute a new hmac and compare it with the actual given hmac.
    """
    api_secret = API_SECRET or ""
    actual_hmac = params["hmac"]
    sorted_query = encode_query_pairs(params)

    calculated_hmac = hmac.new(api_secret.encode("utf-8"),
                               sorted_query.encode("utf-8"),
                               hashlib.sha256).hexdigest()

    return hmac.compare_digest(calculated_hmac, actual_hmac)
