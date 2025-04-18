from ..modules.client import BaseClient

class Client(BaseClient):
    """
    Client class for Power BI API
    """

    def __init__(self,client_id, client_secret, tenant_id, scope):
        super()
        #.__init__()
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.scope = scope