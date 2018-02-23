# swagger_client.WebhooksApi

All URIs are relative to *https://api.upcall.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook**](WebhooksApi.md#create_webhook) | **POST** /webhooks | Create a new webhook
[**delete_webhook**](WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{id} | Delete a webhook
[**fetch_webhook**](WebhooksApi.md#fetch_webhook) | **GET** /webhooks/{id} | Get a specific webhook
[**fetch_webhooks**](WebhooksApi.md#fetch_webhooks) | **GET** /webhooks | Get all webhooks
[**update_webhook**](WebhooksApi.md#update_webhook) | **PATCH** /webhooks/{id} | Update a webhook


# **create_webhook**
> InlineResponse2008 create_webhook(webhook)

Create a new webhook

Create webhook

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
api_instance = swagger_client.WebhooksApi()
webhook = swagger_client.Webhook() # Webhook | Webhook data

try: 
    # Create a new webhook
    api_response = api_instance.create_webhook(webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->create_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook** | [**Webhook**](Webhook.md)| Webhook data | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(id)

Delete a webhook

Delete webhook

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
api_instance = swagger_client.WebhooksApi()
id = 'id_example' # str | ID of webhook

try: 
    # Delete a webhook
    api_instance.delete_webhook(id)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of webhook | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_webhook**
> InlineResponse2008 fetch_webhook(id)

Get a specific webhook

Fetch webhook

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
api_instance = swagger_client.WebhooksApi()
id = 'id_example' # str | ID of webhook

try: 
    # Get a specific webhook
    api_response = api_instance.fetch_webhook(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->fetch_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of webhook | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_webhooks**
> InlineResponse2007 fetch_webhooks(limit=limit, start_id=start_id, end_id=end_id, url=url, kind=kind, sort=sort)

Get all webhooks

Fetch webhooks

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
api_instance = swagger_client.WebhooksApi()
limit = 56 # int | Amount of records to return. 25 by default. (optional)
start_id = 56 # int | Object ID to fetch next page (optional)
end_id = 56 # int | Object ID to fetch previous page (optional)
url = 'url_example' # str | Filter. Filter collection by url (optional)
kind = 'kind_example' # str | Filter. Filter collection by kind (optional)
sort = 'sort_example' # str | Sort field. Available fields: url, kind (optional)

try: 
    # Get all webhooks
    api_response = api_instance.fetch_webhooks(limit=limit, start_id=start_id, end_id=end_id, url=url, kind=kind, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->fetch_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Amount of records to return. 25 by default. | [optional] 
 **start_id** | **int**| Object ID to fetch next page | [optional] 
 **end_id** | **int**| Object ID to fetch previous page | [optional] 
 **url** | **str**| Filter. Filter collection by url | [optional] 
 **kind** | **str**| Filter. Filter collection by kind | [optional] 
 **sort** | **str**| Sort field. Available fields: url, kind | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> InlineResponse2008 update_webhook(id, webhook)

Update a webhook

Update webhook

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
api_instance = swagger_client.WebhooksApi()
id = 'id_example' # str | ID of webhook
webhook = swagger_client.Webhook1() # Webhook1 | Webhook data

try: 
    # Update a webhook
    api_response = api_instance.update_webhook(id, webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->update_webhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of webhook | 
 **webhook** | [**Webhook1**](Webhook1.md)| Webhook data | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

