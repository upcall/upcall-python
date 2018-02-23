# upcall.QuestionsApi

All URIs are relative to *https://api.upcall.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_campaign_questions**](QuestionsApi.md#fetch_campaign_questions) | **GET** /campaigns/{id}/questions | Get campaign&#39;s questions


# **fetch_campaign_questions**
> InlineResponse20010 fetch_campaign_questions(id, limit=limit, start_id=start_id, end_id=end_id)

Get campaign's questions

Fetching questions for campaign

### Example 
```python
from __future__ import print_function
import time
import upcall
from upcall.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
upcall.configuration.api_key['Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# upcall.configuration.api_key_prefix['Token'] = 'Bearer'
# Configure OAuth2 access token for authorization: oauth2
upcall.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = upcall.QuestionsApi()
id = 'id_example' # str | ID of campaign
limit = 56 # int | Amount of records to return. 25 by default. (optional)
start_id = 56 # int | Object ID to fetch next page (optional)
end_id = 56 # int | Object ID to fetch previous page (optional)

try: 
    # Get campaign's questions
    api_response = api_instance.fetch_campaign_questions(id, limit=limit, start_id=start_id, end_id=end_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->fetch_campaign_questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of campaign | 
 **limit** | **int**| Amount of records to return. 25 by default. | [optional] 
 **start_id** | **int**| Object ID to fetch next page | [optional] 
 **end_id** | **int**| Object ID to fetch previous page | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

