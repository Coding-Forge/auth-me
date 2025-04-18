import msal

class BaseClient:

    def __init__(self):
        self.scope = None
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        # self._context = context

    def get_headers(self, graph=False, tenant=False):
        """
        Get the access token for the Power BI API
        """

        # authority = f"https://login.microsoftonline.com/{self.tenant_id}/oauth2/v2.0/token"
        authority = f"https://login.microsoftonline.com/{self.tenant_id}"

        # Create a ConfidentialClientApplication object
        app = msal.ConfidentialClientApplication(
            client_id=self.client_id,
            client_credential=self.client_secret,
            authority=authority
        )


        # This needs to stay as a list
        scopes = [self.scope]
        
        # Acquire a token using client credentials
        try:
            result = app.acquire_token_for_client(scopes=scopes)

            if "access_token" in result:
                access_token = result["access_token"]
                # Use the access token to make API calls to Power BI
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {access_token}'
                }
            else:
                # If silent token acquisition fails, fallback to interactive authentication
                result = app.acquire_token_for_client(scopes=scopes)

                if "access_token" in result:
                    # TODO: Add your Power BI API calls here
                    access_token = result["access_token"]
                    # Use the access token to make API calls to Power BI
                    # headers = {'Authorization': f'Bearer {access_token}'}

                    headers = {
                        'Content-Type': 'application/json',
                        'Authorization': f'Bearer {access_token}'
                    }

                else:
                    print(result.get("error_description", "Authentication failed."))

            return headers
            
        except Exception as ex:
            # self._context.logger.error(f"An exception occurred while reading the file: {str(ex)}")
            print(ex)