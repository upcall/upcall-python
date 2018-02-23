# swagger-client
A RESTful API (json) to manage your human-powered outbound call campaigns.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/upcall/upcall-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/upcall/upcall-python.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.upcall.com/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AnswersApi* | [**fetch_contact_answers**](docs/AnswersApi.md#fetch_contact_answers) | **GET** /contacts/{id}/answers | Get contact&#39;s answers
*AnswersApi* | [**fetch_question_answers**](docs/AnswersApi.md#fetch_question_answers) | **GET** /questions/{id}/answers | Get question&#39;s answers
*CallsApi* | [**fetch_calls**](docs/CallsApi.md#fetch_calls) | **GET** /calls | Get all calls
*CallsApi* | [**fetch_calls_for_campaign**](docs/CallsApi.md#fetch_calls_for_campaign) | **GET** /campaigns/{id}/calls | Get all calls for a campaign
*CampaignsApi* | [**create_campaign**](docs/CampaignsApi.md#create_campaign) | **POST** /campaigns | Create a new campaign
*CampaignsApi* | [**delete_campaign**](docs/CampaignsApi.md#delete_campaign) | **DELETE** /campaigns/{id} | Delete a campaign
*CampaignsApi* | [**fetch_campaign**](docs/CampaignsApi.md#fetch_campaign) | **GET** /campaigns/{id} | Get a specific campaign
*CampaignsApi* | [**fetch_campaigns**](docs/CampaignsApi.md#fetch_campaigns) | **GET** /campaigns | Get all campaigns
*CampaignsApi* | [**update_campaign**](docs/CampaignsApi.md#update_campaign) | **PATCH** /campaigns/{id} | Update a campaign
*ContactsApi* | [**create_contact**](docs/ContactsApi.md#create_contact) | **POST** /campaigns/{id}/contacts | Add a contact to a campaign
*ContactsApi* | [**delete_contact**](docs/ContactsApi.md#delete_contact) | **DELETE** /contacts/{id} | Delete contact
*ContactsApi* | [**fetch_contacts**](docs/ContactsApi.md#fetch_contacts) | **GET** /campaigns/{id}/contacts | Get contacts for a campaign
*ContactsApi* | [**fetch_custom_fields**](docs/ContactsApi.md#fetch_custom_fields) | **GET** /contacts/{id}/custom_fields | Get custom fields
*ContactsApi* | [**fetch_specific_contact**](docs/ContactsApi.md#fetch_specific_contact) | **GET** /contacts/{id} | Get a specific contact
*ContactsApi* | [**update_contact**](docs/ContactsApi.md#update_contact) | **PATCH** /contacts/{id} | Update a contact
*CustomFieldsApi* | [**fetch_custom_fields**](docs/CustomFieldsApi.md#fetch_custom_fields) | **GET** /contacts/{id}/custom_fields | Get custom fields
*OauthAuthorizedApplicationsApi* | [**fetch_oauth_authorized_applications**](docs/OauthAuthorizedApplicationsApi.md#fetch_oauth_authorized_applications) | **GET** /oauth/authorized_applications | 
*OauthAuthorizedApplicationsApi* | [**revoke_oauth_authorized_application**](docs/OauthAuthorizedApplicationsApi.md#revoke_oauth_authorized_application) | **DELETE** /oauth/authorized_applications/{id} | 
*QuestionsApi* | [**fetch_campaign_questions**](docs/QuestionsApi.md#fetch_campaign_questions) | **GET** /campaigns/{id}/questions | Get campaign&#39;s questions
*WebhooksApi* | [**create_webhook**](docs/WebhooksApi.md#create_webhook) | **POST** /webhooks | Create a new webhook
*WebhooksApi* | [**delete_webhook**](docs/WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{id} | Delete a webhook
*WebhooksApi* | [**fetch_webhook**](docs/WebhooksApi.md#fetch_webhook) | **GET** /webhooks/{id} | Get a specific webhook
*WebhooksApi* | [**fetch_webhooks**](docs/WebhooksApi.md#fetch_webhooks) | **GET** /webhooks | Get all webhooks
*WebhooksApi* | [**update_webhook**](docs/WebhooksApi.md#update_webhook) | **PATCH** /webhooks/{id} | Update a webhook


## Documentation For Models

 - [Address](docs/Address.md)
 - [Answer](docs/Answer.md)
 - [Call](docs/Call.md)
 - [Campaign](docs/Campaign.md)
 - [Campaign1](docs/Campaign1.md)
 - [Contact](docs/Contact.md)
 - [Contact1](docs/Contact1.md)
 - [ContactAnswers](docs/ContactAnswers.md)
 - [ContactAttribute](docs/ContactAttribute.md)
 - [Error](docs/Error.md)
 - [ErrorErrors](docs/ErrorErrors.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [Keyvalue](docs/Keyvalue.md)
 - [OauthAuthorizedApplication](docs/OauthAuthorizedApplication.md)
 - [Question](docs/Question.md)
 - [Webhook](docs/Webhook.md)
 - [Webhook1](docs/Webhook1.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Token
- **Location**: HTTP header

## oauth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: https://www.upcall.com/oauth/authorize
- **Scopes**: 
 - **public**: Read/write data


## Author

support@upcall.com

