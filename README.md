# Sentinel Scripts
A place for simple scripts!

# Using the Azure SDK for Python
:link: https://azure.github.io/azure-sdk/releases/latest/all/python.html

## Sentinel SDK
We use the [azure-mgmt-securityinsight](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/securityinsight/azure-mgmt-securityinsight) package to authenticate.

## Authentication and API Instantiation
:link: https://docs.microsoft.com/en-us/azure/developer/python/sdk/authentication-overview

We use the [azure-identity](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity) package to authenticate.

```terminal
pip install azure-identity
```

The simplest way to get an authentication token involves using [DefaultAzureCredential](https://docs.microsoft.com/python/api/azure-identity/azure.identity.defaultazurecredential) which grabs a valid token from your environment. See the link for details.

It can be used as follows:

```python
from azure.identity import DefaultAzureCredential
from azure.mgmt.securityinsight import SecurityInsights

subscription_id = "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"

# Acquire a credential object
credential = DefaultAzureCredential()


# Authenticate to an API provider (e.g. Sentinel)
sentinel = SecurityInsights(credential, subscription_id)
```

