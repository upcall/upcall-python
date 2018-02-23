# swagger_client.ContactsApi

All URIs are relative to *https://api.upcall.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact**](ContactsApi.md#create_contact) | **POST** /campaigns/{id}/contacts | Add a contact to a campaign
[**delete_contact**](ContactsApi.md#delete_contact) | **DELETE** /contacts/{id} | Delete contact
[**fetch_contacts**](ContactsApi.md#fetch_contacts) | **GET** /campaigns/{id}/contacts | Get contacts for a campaign
[**fetch_custom_fields**](ContactsApi.md#fetch_custom_fields) | **GET** /contacts/{id}/custom_fields | Get custom fields
[**fetch_specific_contact**](ContactsApi.md#fetch_specific_contact) | **GET** /contacts/{id} | Get a specific contact
[**update_contact**](ContactsApi.md#update_contact) | **PATCH** /contacts/{id} | Update a contact


# **create_contact**
> InlineResponse2003 create_contact(id, contact, custom_fields=custom_fields)

Add a contact to a campaign

Create contact for campaign

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
api_instance = swagger_client.ContactsApi()
id = 'id_example' # str | ID of campaign
contact = swagger_client.Contact() # Contact | Contact data
custom_fields = true # bool | If set, custom fields will be displayed in the output (optional)

try: 
    # Add a contact to a campaign
    api_response = api_instance.create_contact(id, contact, custom_fields=custom_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of campaign | 
 **contact** | [**Contact**](Contact.md)| Contact data | 
 **custom_fields** | **bool**| If set, custom fields will be displayed in the output | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(id)

Delete contact

Delete contact

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
api_instance = swagger_client.ContactsApi()
id = 'id_example' # str | ID of contact to delete

try: 
    # Delete contact
    api_instance.delete_contact(id)
except ApiException as e:
    print("Exception when calling ContactsApi->delete_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of contact to delete | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_contacts**
> InlineResponse2002 fetch_contacts(id, limit=limit, start_id=start_id, end_id=end_id, first_name=first_name, last_name=last_name, company=company, name=name, field_id=field_id, urgency=urgency, status=status, phone=phone, email=email, sort=sort, custom_fields=custom_fields, answers=answers)

Get contacts for a campaign

Fetching contacts for campaign

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
api_instance = swagger_client.ContactsApi()
id = 'id_example' # str | ID of campaign
limit = 56 # int | Amount of records to return. 25 by default. (optional)
start_id = 56 # int | Object ID to fetch next page (optional)
end_id = 56 # int | Object ID to fetch previous page (optional)
first_name = 'first_name_example' # str | Filter. Filter collection by first_name (optional)
last_name = 'last_name_example' # str | Filter. Filter collection by last_name (optional)
company = 'company_example' # str | Filter. Filter collection by company (optional)
name = 'name_example' # str | Filter. Filter collection by name (optional)
field_id = 'field_id_example' # str | Filter. Filter collection by field_id (optional)
urgency = 'urgency_example' # str | Filter. Filter collection by urgency (optional)
status = 'status_example' # str | Filter. Filter collection by status (optional)
phone = 'phone_example' # str | Filter. Filter collection by phone (optional)
email = 'email_example' # str | Filter. Filter collection by email (optional)
sort = 'sort_example' # str | Sort field. Available fields: last_name, first_name, company, calls.status                              calls.called_at, calls.caller.user.first_name, calls.caller.user.last_name, urgency (optional)
custom_fields = true # bool | If set, custom fields will be displayed in the output (optional)
answers = true # bool | If set, question/answer pairs will be displayed in the output (optional)

try: 
    # Get contacts for a campaign
    api_response = api_instance.fetch_contacts(id, limit=limit, start_id=start_id, end_id=end_id, first_name=first_name, last_name=last_name, company=company, name=name, field_id=field_id, urgency=urgency, status=status, phone=phone, email=email, sort=sort, custom_fields=custom_fields, answers=answers)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->fetch_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of campaign | 
 **limit** | **int**| Amount of records to return. 25 by default. | [optional] 
 **start_id** | **int**| Object ID to fetch next page | [optional] 
 **end_id** | **int**| Object ID to fetch previous page | [optional] 
 **first_name** | **str**| Filter. Filter collection by first_name | [optional] 
 **last_name** | **str**| Filter. Filter collection by last_name | [optional] 
 **company** | **str**| Filter. Filter collection by company | [optional] 
 **name** | **str**| Filter. Filter collection by name | [optional] 
 **field_id** | **str**| Filter. Filter collection by field_id | [optional] 
 **urgency** | **str**| Filter. Filter collection by urgency | [optional] 
 **status** | **str**| Filter. Filter collection by status | [optional] 
 **phone** | **str**| Filter. Filter collection by phone | [optional] 
 **email** | **str**| Filter. Filter collection by email | [optional] 
 **sort** | **str**| Sort field. Available fields: last_name, first_name, company, calls.status                              calls.called_at, calls.caller.user.first_name, calls.caller.user.last_name, urgency | [optional] 
 **custom_fields** | **bool**| If set, custom fields will be displayed in the output | [optional] 
 **answers** | **bool**| If set, question/answer pairs will be displayed in the output | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_custom_fields**
> InlineResponse2006 fetch_custom_fields(id, limit=limit, start_id=start_id, end_id=end_id)

Get custom fields

Fetching custom fields for contact

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
api_instance = swagger_client.ContactsApi()
id = 'id_example' # str | ID of contact
limit = 56 # int | Amount of records to return. 25 by default. (optional)
start_id = 56 # int | Object ID to fetch next page (optional)
end_id = 56 # int | Object ID to fetch previous page (optional)

try: 
    # Get custom fields
    api_response = api_instance.fetch_custom_fields(id, limit=limit, start_id=start_id, end_id=end_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->fetch_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of contact | 
 **limit** | **int**| Amount of records to return. 25 by default. | [optional] 
 **start_id** | **int**| Object ID to fetch next page | [optional] 
 **end_id** | **int**| Object ID to fetch previous page | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_specific_contact**
> InlineResponse2003 fetch_specific_contact(id, custom_fields=custom_fields)

Get a specific contact

Fetch specific contact

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
api_instance = swagger_client.ContactsApi()
id = 'id_example' # str | ID of contact to fetch
custom_fields = true # bool | If set, custom fields will be displayed in the output (optional)

try: 
    # Get a specific contact
    api_response = api_instance.fetch_specific_contact(id, custom_fields=custom_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->fetch_specific_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of contact to fetch | 
 **custom_fields** | **bool**| If set, custom fields will be displayed in the output | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> InlineResponse2003 update_contact(id, contact, custom_fields=custom_fields)

Update a contact

Update contact

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
api_instance = swagger_client.ContactsApi()
id = 'id_example' # str | ID of contact to update
contact = swagger_client.Contact1() # Contact1 | Contact data
custom_fields = true # bool | If set, custom fields will be displayed in the output (optional)

try: 
    # Update a contact
    api_response = api_instance.update_contact(id, contact, custom_fields=custom_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of contact to update | 
 **contact** | [**Contact1**](Contact1.md)| Contact data | 
 **custom_fields** | **bool**| If set, custom fields will be displayed in the output | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

