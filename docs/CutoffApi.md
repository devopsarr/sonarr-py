# sonarr.CutoffApi

All URIs are relative to *http://localhost:8989*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_wanted_cutoff**](CutoffApi.md#get_wanted_cutoff) | **GET** /api/v3/wanted/cutoff | 
[**get_wanted_cutoff_by_id**](CutoffApi.md#get_wanted_cutoff_by_id) | **GET** /api/v3/wanted/cutoff/{id} | 


# **get_wanted_cutoff**
> EpisodeResourcePagingResource get_wanted_cutoff(page=page, page_size=page_size, sort_key=sort_key, sort_direction=sort_direction, include_series=include_series, include_episode_file=include_episode_file, include_images=include_images, monitored=monitored)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import sonarr
from sonarr.models.episode_resource_paging_resource import EpisodeResourcePagingResource
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
    api_instance = sonarr.CutoffApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)
    sort_key = 'sort_key_example' # str |  (optional)
    sort_direction = sonarr.SortDirection() # SortDirection |  (optional)
    include_series = False # bool |  (optional) (default to False)
    include_episode_file = False # bool |  (optional) (default to False)
    include_images = False # bool |  (optional) (default to False)
    monitored = True # bool |  (optional) (default to True)

    try:
        api_response = api_instance.get_wanted_cutoff(page=page, page_size=page_size, sort_key=sort_key, sort_direction=sort_direction, include_series=include_series, include_episode_file=include_episode_file, include_images=include_images, monitored=monitored)
        print("The response of CutoffApi->get_wanted_cutoff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CutoffApi->get_wanted_cutoff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **sort_key** | **str**|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **include_series** | **bool**|  | [optional] [default to False]
 **include_episode_file** | **bool**|  | [optional] [default to False]
 **include_images** | **bool**|  | [optional] [default to False]
 **monitored** | **bool**|  | [optional] [default to True]

### Return type

[**EpisodeResourcePagingResource**](EpisodeResourcePagingResource.md)

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

# **get_wanted_cutoff_by_id**
> EpisodeResource get_wanted_cutoff_by_id(id)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import sonarr
from sonarr.models.episode_resource import EpisodeResource
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
    api_instance = sonarr.CutoffApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_wanted_cutoff_by_id(id)
        print("The response of CutoffApi->get_wanted_cutoff_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CutoffApi->get_wanted_cutoff_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EpisodeResource**](EpisodeResource.md)

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

