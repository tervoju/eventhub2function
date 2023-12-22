import os
import logging

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


def get_secret(credential: DefaultAzureCredential, secret_name: str) -> str:
    # Azure Key Vault details
    # key_vault_name = os.environ["KEYVAULT_NAME"]
    key_vault_url = os.environ["KEY_VAULT_URL"]

    # Create a SecretClient
    client = SecretClient(vault_url=key_vault_url, credential=credential)

    # Retrieve the secret from Azure Key Vault
    secret = client.get_secret(secret_name)
    auth_token = secret.value

    if not auth_token:
        logging.error("The get_secret() returned None")

    return auth_token
