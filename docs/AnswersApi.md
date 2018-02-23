# swagger_client.AnswersApi

All URIs are relative to *https://api.upcall.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetch_contact_answers**](AnswersApi.md#fetch_contact_answers) | **GET** /contacts/{id}/answers | Get contact&#39;s answers
[**fetch_question_answers**](AnswersApi.md#fetch_question_answers) | **GET** /questions/{id}/answers | Get question&#39;s answers


# **fetch_contact_answers**
> InlineResponse2005 fetch_contact_answers(id, limit=limit, start_id=start_id, end_id=end_id, result=result, sort=sort)

Get contact's answers

Fetching answers for contact

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
api_instance = swagger_client.AnswersApi()
id = 'id_example' # str | ID of contact
limit = 56 # int | Amount of records to return. 25 by default. (optional)
start_id = 56 # int | Object ID to fetch next page (optional)
end_id = 56 # int | Object ID to fetch previous page (optional)
result = 'result_example' # str | Filter. Filter collection by result (optional)
sort = 'sort_example' # str | Sort field. Available fields: answer_type, created_at (optional)

try: 
    # Get contact's answers
    api_response = api_instance.fetch_contact_answers(id, limit=limit, start_id=start_id, end_id=end_id, result=result, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnswersApi->fetch_contact_answers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of contact | 
 **limit** | **int**| Amount of records to return. 25 by default. | [optional] 
 **start_id** | **int**| Object ID to fetch next page | [optional] 
 **end_id** | **int**| Object ID to fetch previous page | [optional] 
 **result** | **str**| Filter. Filter collection by result | [optional] 
 **sort** | **str**| Sort field. Available fields: answer_type, created_at | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_question_answers**
> InlineResponse2005 fetch_question_answers(id, limit=limit, start_id=start_id, end_id=end_id, result=result, sort=sort)

Get question's answers

Fetching answers for question

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
api_instance = swagger_client.AnswersApi()
id = 'id_example' # str | ID of question
limit = 56 # int | Amount of records to return. 25 by default. (optional)
start_id = 56 # int | Object ID to fetch next page (optional)
end_id = 56 # int | Object ID to fetch previous page (optional)
result = 'result_example' # str | Filter. Filter collection by result (optional)
sort = 'sort_example' # str | Sort field. Available fields: created_at (optional)

try: 
    # Get question's answers
    api_response = api_instance.fetch_question_answers(id, limit=limit, start_id=start_id, end_id=end_id, result=result, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnswersApi->fetch_question_answers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of question | 
 **limit** | **int**| Amount of records to return. 25 by default. | [optional] 
 **start_id** | **int**| Object ID to fetch next page | [optional] 
 **end_id** | **int**| Object ID to fetch previous page | [optional] 
 **result** | **str**| Filter. Filter collection by result | [optional] 
 **sort** | **str**| Sort field. Available fields: created_at | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

