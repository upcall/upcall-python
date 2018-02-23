# swagger_client.OauthAuthorizedApplicationsApi

All URIs are relative to *https://api.upcall.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_oauth_authorized_applications**](OauthAuthorizedApplicationsApi.md#fetch_oauth_authorized_applications) | **GET** /oauth/authorized_applications | 
[**revoke_oauth_authorized_application**](OauthAuthorizedApplicationsApi.md#revoke_oauth_authorized_application) | **DELETE** /oauth/authorized_applications/{id} | 


# **fetch_oauth_authorized_applications**
> InlineResponse2009 fetch_oauth_authorized_applications()



Fetch Oauth authorized applications

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Token'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.OauthAuthorizedApplicationsApi()

try: 
    api_response = api_instance.fetch_oauth_authorized_applications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OauthAuthorizedApplicationsApi->fetch_oauth_authorized_applications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_oauth_authorized_application**
> revoke_oauth_authorized_application(id)



Revoke Oauth authorized application

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
swagger_client.configuration.api_key['Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Token'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.OauthAuthorizedApplicationsApi()
id = 'id_example' # str | ID of authorized application

try: 
    api_instance.revoke_oauth_authorized_application(id)
except ApiException as e:
    print("Exception when calling OauthAuthorizedApplicationsApi->revoke_oauth_authorized_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of authorized application | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

