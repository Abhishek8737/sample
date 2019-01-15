from ecom.authentication.http_authentication import *
from ecom.authentication.no_authentication import *
from ecom.authentication.http_inter_service_auth_v2 import *
from ecom.authentication.http_multi_authentication import *
#when import no_authentication was before http_authentication- resulted in import error
#ImportError: cannot import name 'HTTPAuthentication' in no_authentication.py

no_auth = NoAuthentication()
v2_auth = HTTPInterServiceAuthV2()


authenticator = MultiAuthentication(no_auth, v2_auth)
