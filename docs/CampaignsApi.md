# upcall.CampaignsApi

All URIs are relative to *https://api.upcall.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_campaign**](CampaignsApi.md#create_campaign) | **POST** /campaigns | Create a new campaign
[**delete_campaign**](CampaignsApi.md#delete_campaign) | **DELETE** /campaigns/{id} | Delete a campaign
[**fetch_campaign**](CampaignsApi.md#fetch_campaign) | **GET** /campaigns/{id} | Get a specific campaign
[**fetch_campaigns**](CampaignsApi.md#fetch_campaigns) | **GET** /campaigns | Get all campaigns
[**update_campaign**](CampaignsApi.md#update_campaign) | **PATCH** /campaigns/{id} | Update a campaign


# **create_campaign**
> InlineResponse2001 create_campaign(campaign)

Create a new campaign

Create campaign

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
api_instance = upcall.CampaignsApi()
campaign = upcall.Campaign() # Campaign | Campaign data

try: 
    # Create a new campaign
    api_response = api_instance.create_campaign(campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->create_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign** | [**Campaign**](Campaign.md)| Campaign data | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_campaign**
> delete_campaign(id)

Delete a campaign

Delete campaign

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
api_instance = upcall.CampaignsApi()
id = 'id_example' # str | ID of campaign

try: 
    # Delete a campaign
    api_instance.delete_campaign(id)
except ApiException as e:
    print("Exception when calling CampaignsApi->delete_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of campaign | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_campaign**
> InlineResponse2001 fetch_campaign(id)

Get a specific campaign

Fetch a campaign

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
api_instance = upcall.CampaignsApi()
id = 'id_example' # str | ID of campaign

try: 
    # Get a specific campaign
    api_response = api_instance.fetch_campaign(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->fetch_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of campaign | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_campaigns**
> InlineResponse200 fetch_campaigns(limit=limit, start_id=start_id, end_id=end_id, name=name, status=status, language=language, min_start_date=min_start_date, max_start_date=max_start_date, min_created_datetime=min_created_datetime, max_created_datetime=max_created_datetime, min_updated_datetime=min_updated_datetime, max_updated_datetime=max_updated_datetime, sort=sort)

Get all campaigns

Fetch campaigns

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
api_instance = upcall.CampaignsApi()
limit = 56 # int | Amount of records to return. 25 by default. (optional)
start_id = 56 # int | Object ID to fetch next page (optional)
end_id = 56 # int | Object ID to fetch previous page (optional)
name = 'name_example' # str | Filter. Filter collection by name (optional)
status = 'status_example' # str | Filter. Filter collection by status (optional)
language = 'language_example' # str | Filter. Filter collection by language (optional)
min_start_date = '2013-10-20' # date | Filter. Format: YYYY-MM-DD. Filter collection by min_start_date, required max_start_date too. (optional)
max_start_date = '2013-10-20' # date | Filter. Format: YYYY-MM-DD. Filter collection by max_start_date, required mix_start_date too. (optional)
min_created_datetime = '2013-10-20T19:20:30+01:00' # datetime | Filter. Format: YYYY-MM-DDTHH:MM:SS. Filter collection by min_created_datetime, required max_created_datetime too. (optional)
max_created_datetime = '2013-10-20T19:20:30+01:00' # datetime | Filter. Format: YYYY-MM-DDTHH:MM:SS. Filter collection by max_created_datetime, required min_created_datetime too. (optional)
min_updated_datetime = '2013-10-20T19:20:30+01:00' # datetime | Filter. Format: YYYY-MM-DDTHH:MM:SS. Filter collection by min_updated_datetime, required max_updated_datetime too. (optional)
max_updated_datetime = '2013-10-20T19:20:30+01:00' # datetime | Filter. Format: YYYY-MM-DDTHH:MM:SS. Filter collection by max_updated_datetime, required min_updated_datetime too. (optional)
sort = 'sort_example' # str | Sort field. Available fields: name, status, kind, created_at, start_date (optional)

try: 
    # Get all campaigns
    api_response = api_instance.fetch_campaigns(limit=limit, start_id=start_id, end_id=end_id, name=name, status=status, language=language, min_start_date=min_start_date, max_start_date=max_start_date, min_created_datetime=min_created_datetime, max_created_datetime=max_created_datetime, min_updated_datetime=min_updated_datetime, max_updated_datetime=max_updated_datetime, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->fetch_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Amount of records to return. 25 by default. | [optional] 
 **start_id** | **int**| Object ID to fetch next page | [optional] 
 **end_id** | **int**| Object ID to fetch previous page | [optional] 
 **name** | **str**| Filter. Filter collection by name | [optional] 
 **status** | **str**| Filter. Filter collection by status | [optional] 
 **language** | **str**| Filter. Filter collection by language | [optional] 
 **min_start_date** | **date**| Filter. Format: YYYY-MM-DD. Filter collection by min_start_date, required max_start_date too. | [optional] 
 **max_start_date** | **date**| Filter. Format: YYYY-MM-DD. Filter collection by max_start_date, required mix_start_date too. | [optional] 
 **min_created_datetime** | **datetime**| Filter. Format: YYYY-MM-DDTHH:MM:SS. Filter collection by min_created_datetime, required max_created_datetime too. | [optional] 
 **max_created_datetime** | **datetime**| Filter. Format: YYYY-MM-DDTHH:MM:SS. Filter collection by max_created_datetime, required min_created_datetime too. | [optional] 
 **min_updated_datetime** | **datetime**| Filter. Format: YYYY-MM-DDTHH:MM:SS. Filter collection by min_updated_datetime, required max_updated_datetime too. | [optional] 
 **max_updated_datetime** | **datetime**| Filter. Format: YYYY-MM-DDTHH:MM:SS. Filter collection by max_updated_datetime, required min_updated_datetime too. | [optional] 
 **sort** | **str**| Sort field. Available fields: name, status, kind, created_at, start_date | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_campaign**
> InlineResponse2001 update_campaign(id, campaign)

Update a campaign

Update campaign

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
api_instance = upcall.CampaignsApi()
id = 'id_example' # str | ID of campaign
campaign = upcall.Campaign1() # Campaign1 | Campaign data

try: 
    # Update a campaign
    api_response = api_instance.update_campaign(id, campaign)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CampaignsApi->update_campaign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of campaign | 
 **campaign** | [**Campaign1**](Campaign1.md)| Campaign data | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

