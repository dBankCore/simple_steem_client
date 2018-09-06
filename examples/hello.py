
from simple_dpay_client.client import DPayRemoteBackend, DPayInterface

import json

backend = DPayRemoteBackend(nodes=["http://127.0.0.1:9990/"], appbase=True)
dpay = DPayInterface(backend)

dgpo = dpay.database_api.get_dynamic_global_properties()

print("dgpo:", json.dumps(dgpo, separators=(",", ":")))
