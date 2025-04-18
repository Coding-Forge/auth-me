from utils import Client
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def main():
    """
    Main function to authorize the client
    """
    # Create a client instance

    print(f"Client Id: {os.getenv('CLIENT_ID', [])}")

    client = Client(
        client_id=os.getenv("CLIENT_ID", []),
        client_secret=os.getenv("CLIENT_SECRET", []),
        tenant_id=os.getenv("TENANT_ID", []),
        scope="https://analysis.windows.net/powerbi/api/.default"
    )     

    headers = client.get_headers()

    print(f"Headers: {headers}")


if __name__ == "__main__":
    main()

