# sonarr.ImportListExclusionApi

All URIs are relative to *http://localhost:8989*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_import_list_exclusion**](ImportListExclusionApi.md#create_import_list_exclusion) | **POST** /api/v3/importlistexclusion | 
[**delete_import_list_exclusion**](ImportListExclusionApi.md#delete_import_list_exclusion) | **DELETE** /api/v3/importlistexclusion/{id} | 
[**delete_import_list_exclusion_bulk**](ImportListExclusionApi.md#delete_import_list_exclusion_bulk) | **DELETE** /api/v3/importlistexclusion/bulk | 
[**get_import_list_exclusion_by_id**](ImportListExclusionApi.md#get_import_list_exclusion_by_id) | **GET** /api/v3/importlistexclusion/{id} | 
[**get_import_list_exclusion_paged**](ImportListExclusionApi.md#get_import_list_exclusion_paged) | **GET** /api/v3/importlistexclusion/paged | 
[**list_import_list_exclusion**](ImportListExclusionApi.md#list_import_list_exclusion) | **GET** /api/v3/importlistexclusion | 
[**update_import_list_exclusion**](ImportListExclusionApi.md#update_import_list_exclusion) | **PUT** /api/v3/importlistexclusion/{id} | 


# **create_import_list_exclusion**
> ImportListExclusionResource create_import_list_exclusion(import_list_exclusion_resource=import_list_exclusion_resource)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import sonarr
from sonarr.models.import_list_exclusion_resource import ImportListExclusionResource
from sonarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8989
# See configuration.py for a list of all supported configuration parameters.
configuration = sonarr.Configuration(
    host = "http://localhost:8989"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with sonarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sonarr.ImportListExclusionApi(api_client)
    import_list_exclusion_resource = sonarr.ImportListExclusionResource() # ImportListExclusionResource |  (optional)

    try:
        api_response = api_instance.create_import_list_exclusion(import_list_exclusion_resource=import_list_exclusion_resource)
        print("The response of ImportListExclusionApi->create_import_list_exclusion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportListExclusionApi->create_import_list_exclusion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_list_exclusion_resource** | [**ImportListExclusionResource**](ImportListExclusionResource.md)|  | [optional] 

### Return type

[**ImportListExclusionResource**](ImportListExclusionResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_import_list_exclusion**
> delete_import_list_exclusion(id)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import sonarr
from sonarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8989
# See configuration.py for a list of all supported configuration parameters.
configuration = sonarr.Configuration(
    host = "http://localhost:8989"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with sonarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sonarr.ImportListExclusionApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_import_list_exclusion(id)
    except Exception as e:
        print("Exception when calling ImportListExclusionApi->delete_import_list_exclusion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_import_list_exclusion_bulk**
> delete_import_list_exclusion_bulk(import_list_exclusion_bulk_resource=import_list_exclusion_bulk_resource)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import sonarr
from sonarr.models.import_list_exclusion_bulk_resource import ImportListExclusionBulkResource
from sonarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8989
# See configuration.py for a list of all supported configuration parameters.
configuration = sonarr.Configuration(
    host = "http://localhost:8989"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with sonarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sonarr.ImportListExclusionApi(api_client)
    import_list_exclusion_bulk_resource = sonarr.ImportListExclusionBulkResource() # ImportListExclusionBulkResource |  (optional)

    try:
        api_instance.delete_import_list_exclusion_bulk(import_list_exclusion_bulk_resource=import_list_exclusion_bulk_resource)
    except Exception as e:
        print("Exception when calling ImportListExclusionApi->delete_import_list_exclusion_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_list_exclusion_bulk_resource** | [**ImportListExclusionBulkResource**](ImportListExclusionBulkResource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_list_exclusion_by_id**
> ImportListExclusionResource get_import_list_exclusion_by_id(id)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import sonarr
from sonarr.models.import_list_exclusion_resource import ImportListExclusionResource
from sonarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8989
# See configuration.py for a list of all supported configuration parameters.
configuration = sonarr.Configuration(
    host = "http://localhost:8989"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with sonarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sonarr.ImportListExclusionApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_import_list_exclusion_by_id(id)
        print("The response of ImportListExclusionApi->get_import_list_exclusion_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportListExclusionApi->get_import_list_exclusion_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ImportListExclusionResource**](ImportListExclusionResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_list_exclusion_paged**
> ImportListExclusionResourcePagingResource get_import_list_exclusion_paged(page=page, page_size=page_size, sort_key=sort_key, sort_direction=sort_direction)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import sonarr
from sonarr.models.import_list_exclusion_resource_paging_resource import ImportListExclusionResourcePagingResource
from sonarr.models.sort_direction import SortDirection
from sonarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8989
# See configuration.py for a list of all supported configuration parameters.
configuration = sonarr.Configuration(
    host = "http://localhost:8989"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with sonarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sonarr.ImportListExclusionApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)
    sort_key = 'sort_key_example' # str |  (optional)
    sort_direction = sonarr.SortDirection() # SortDirection |  (optional)

    try:
        api_response = api_instance.get_import_list_exclusion_paged(page=page, page_size=page_size, sort_key=sort_key, sort_direction=sort_direction)
        print("The response of ImportListExclusionApi->get_import_list_exclusion_paged:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportListExclusionApi->get_import_list_exclusion_paged: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **sort_key** | **str**|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 

### Return type

[**ImportListExclusionResourcePagingResource**](ImportListExclusionResourcePagingResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_import_list_exclusion**
> List[ImportListExclusionResource] list_import_list_exclusion()

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import sonarr
from sonarr.models.import_list_exclusion_resource import ImportListExclusionResource
from sonarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8989
# See configuration.py for a list of all supported configuration parameters.
configuration = sonarr.Configuration(
    host = "http://localhost:8989"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with sonarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sonarr.ImportListExclusionApi(api_client)

    try:
        api_response = api_instance.list_import_list_exclusion()
        print("The response of ImportListExclusionApi->list_import_list_exclusion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportListExclusionApi->list_import_list_exclusion: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ImportListExclusionResource]**](ImportListExclusionResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_import_list_exclusion**
> ImportListExclusionResource update_import_list_exclusion(id, import_list_exclusion_resource=import_list_exclusion_resource)

### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import sonarr
from sonarr.models.import_list_exclusion_resource import ImportListExclusionResource
from sonarr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8989
# See configuration.py for a list of all supported configuration parameters.
configuration = sonarr.Configuration(
    host = "http://localhost:8989"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with sonarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sonarr.ImportListExclusionApi(api_client)
    id = 'id_example' # str | 
    import_list_exclusion_resource = sonarr.ImportListExclusionResource() # ImportListExclusionResource |  (optional)

    try:
        api_response = api_instance.update_import_list_exclusion(id, import_list_exclusion_resource=import_list_exclusion_resource)
        print("The response of ImportListExclusionApi->update_import_list_exclusion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ImportListExclusionApi->update_import_list_exclusion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **import_list_exclusion_resource** | [**ImportListExclusionResource**](ImportListExclusionResource.md)|  | [optional] 

### Return type

[**ImportListExclusionResource**](ImportListExclusionResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

