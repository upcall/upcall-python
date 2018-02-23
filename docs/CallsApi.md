# swagger_client.CallsApi

All URIs are relative to *https://api.upcall.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_calls**](CallsApi.md#fetch_calls) | **GET** /calls | Get all calls
[**fetch_calls_for_campaign**](CallsApi.md#fetch_calls_for_campaign) | **GET** /campaigns/{id}/calls | Get all calls for a campaign


# **fetch_calls**
> InlineResponse2004 fetch_calls(limit=limit, start_id=start_id, end_id=end_id, status=status, caller_name=caller_name, sort=sort)

Get all calls

Fetching calls for company

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
api_instance = swagger_client.CallsApi()
limit = 56 # int | Amount of records to return. 25 by default. (optional)
start_id = 56 # int | Object ID to fetch next page (optional)
end_id = 56 # int | Object ID to fetch previous page (optional)
status = 'status_example' # str | Filter. Filter collection by status (optional)
caller_name = 'caller_name_example' # str | Filter. Filter collection by caller name (optional)
sort = 'sort_example' # str | Sort field. Available fields: status, called_at (optional)

try: 
    # Get all calls
    api_response = api_instance.fetch_calls(limit=limit, start_id=start_id, end_id=end_id, status=status, caller_name=caller_name, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->fetch_calls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Amount of records to return. 25 by default. | [optional] 
 **start_id** | **int**| Object ID to fetch next page | [optional] 
 **end_id** | **int**| Object ID to fetch previous page | [optional] 
 **status** | **str**| Filter. Filter collection by status | [optional] 
 **caller_name** | **str**| Filter. Filter collection by caller name | [optional] 
 **sort** | **str**| Sort field. Available fields: status, called_at | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_calls_for_campaign**
> InlineResponse2004 fetch_calls_for_campaign(id, limit=limit, start_id=start_id, end_id=end_id, status=status, caller_name=caller_name, sort=sort)

Get all calls for a campaign

Fetching calls for campaign

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
api_instance = swagger_client.CallsApi()
id = 'id_example' # str | ID of campaign
limit = 56 # int | Amount of records to return. 25 by default. (optional)
start_id = 56 # int | Object ID to fetch next page (optional)
end_id = 56 # int | Object ID to fetch previous page (optional)
status = 'status_example' # str | Filter. Filter collection by status (optional)
caller_name = 'caller_name_example' # str | Filter. Filter collection by caller name (optional)
sort = 'sort_example' # str | Sort field. Available fields: status, called_at (optional)

try: 
    # Get all calls for a campaign
    api_response = api_instance.fetch_calls_for_campaign(id, limit=limit, start_id=start_id, end_id=end_id, status=status, caller_name=caller_name, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CallsApi->fetch_calls_for_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of campaign | 
 **limit** | **int**| Amount of records to return. 25 by default. | [optional] 
 **start_id** | **int**| Object ID to fetch next page | [optional] 
 **end_id** | **int**| Object ID to fetch previous page | [optional] 
 **status** | **str**| Filter. Filter collection by status | [optional] 
 **caller_name** | **str**| Filter. Filter collection by caller name | [optional] 
 **sort** | **str**| Sort field. Available fields: status, called_at | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

