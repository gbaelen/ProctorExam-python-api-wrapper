import json
import hashlib
import hmac
import base64

def create_base_string(data):
    values          = []
    key_sorted_data = list(data.items())
    key_sorted_data.sort()

    for key, value in key_sorted_data:
        if type( value ) is list:
            value = json.dumps( value )

        values.append( str( key ) + "=" + str( value ) )

    return "?".join( values )

def create_signature(data, secret):
    base_string = create_base_string( data )
    digest     = hmac.new( bytes( secret, 'utf-8' ),
                     bytes( '', 'utf-8' ),
                     hashlib.sha256 )

    digest.update( bytes( base_string, 'utf-8' ) )

    return base_string, digest.hexdigest()
