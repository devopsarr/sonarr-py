# sonarr.HistoryApi

All URIs are relative to *http://localhost:8989*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_history_failed_by_id**](HistoryApi.md#create_history_failed_by_id) | **POST** /api/v3/history/failed/{id} | 
[**get_history**](HistoryApi.md#get_history) | **GET** /api/v3/history | 
[**list_history_series**](HistoryApi.md#list_history_series) | **GET** /api/v3/history/series | 
[**list_history_since**](HistoryApi.md#list_history_since) | **GET** /api/v3/history/since | 


# **create_history_failed_by_id**
> create_history_failed_by_id(id)



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
    api_instance = sonarr.HistoryApi(api_client)
    id = 56 # int | 

    try:
        api_instance.create_history_failed_by_id(id)
    except Exception as e:
        print("Exception when calling HistoryApi->create_history_failed_by_id: %s\n" % e)
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

# **get_history**
> HistoryResourcePagingResource get_history(page=page, page_size=page_size, sort_key=sort_key, sort_direction=sort_direction, include_series=include_series, include_episode=include_episode, event_type=event_type, episode_id=episode_id, download_id=download_id, series_ids=series_ids, languages=languages, quality=quality)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import sonarr
from sonarr.models.history_resource_paging_resource import HistoryResourcePagingResource
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
    api_instance = sonarr.HistoryApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    page_size = 10 # int |  (optional) (default to 10)
    sort_key = 'sort_key_example' # str |  (optional)
    sort_direction = sonarr.SortDirection() # SortDirection |  (optional)
    include_series = True # bool |  (optional)
    include_episode = True # bool |  (optional)
    event_type = [56] # List[int] |  (optional)
    episode_id = 56 # int |  (optional)
    download_id = 'download_id_example' # str |  (optional)
    series_ids = [56] # List[int] |  (optional)
    languages = [56] # List[int] |  (optional)
    quality = [56] # List[int] |  (optional)

    try:
        api_response = api_instance.get_history(page=page, page_size=page_size, sort_key=sort_key, sort_direction=sort_direction, include_series=include_series, include_episode=include_episode, event_type=event_type, episode_id=episode_id, download_id=download_id, series_ids=series_ids, languages=languages, quality=quality)
        print("The response of HistoryApi->get_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->get_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]
 **sort_key** | **str**|  | [optional] 
 **sort_direction** | [**SortDirection**](.md)|  | [optional] 
 **include_series** | **bool**|  | [optional] 
 **include_episode** | **bool**|  | [optional] 
 **event_type** | [**List[int]**](int.md)|  | [optional] 
 **episode_id** | **int**|  | [optional] 
 **download_id** | **str**|  | [optional] 
 **series_ids** | [**List[int]**](int.md)|  | [optional] 
 **languages** | [**List[int]**](int.md)|  | [optional] 
 **quality** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**HistoryResourcePagingResource**](HistoryResourcePagingResource.md)

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

# **list_history_series**
> List[HistoryResource] list_history_series(series_id=series_id, season_number=season_number, event_type=event_type, include_series=include_series, include_episode=include_episode)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import sonarr
from sonarr.models.episode_history_event_type import EpisodeHistoryEventType
from sonarr.models.history_resource import HistoryResource
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
    api_instance = sonarr.HistoryApi(api_client)
    series_id = 56 # int |  (optional)
    season_number = 56 # int |  (optional)
    event_type = sonarr.EpisodeHistoryEventType() # EpisodeHistoryEventType |  (optional)
    include_series = False # bool |  (optional) (default to False)
    include_episode = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.list_history_series(series_id=series_id, season_number=season_number, event_type=event_type, include_series=include_series, include_episode=include_episode)
        print("The response of HistoryApi->list_history_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->list_history_series: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | [optional] 
 **season_number** | **int**|  | [optional] 
 **event_type** | [**EpisodeHistoryEventType**](.md)|  | [optional] 
 **include_series** | **bool**|  | [optional] [default to False]
 **include_episode** | **bool**|  | [optional] [default to False]

### Return type

[**List[HistoryResource]**](HistoryResource.md)

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

# **list_history_since**
> List[HistoryResource] list_history_since(var_date=var_date, event_type=event_type, include_series=include_series, include_episode=include_episode)



### Example

* Api Key Authentication (apikey):
* Api Key Authentication (X-Api-Key):

```python
import sonarr
from sonarr.models.episode_history_event_type import EpisodeHistoryEventType
from sonarr.models.history_resource import HistoryResource
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
    api_instance = sonarr.HistoryApi(api_client)
    var_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    event_type = sonarr.EpisodeHistoryEventType() # EpisodeHistoryEventType |  (optional)
    include_series = False # bool |  (optional) (default to False)
    include_episode = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.list_history_since(var_date=var_date, event_type=event_type, include_series=include_series, include_episode=include_episode)
        print("The response of HistoryApi->list_history_since:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HistoryApi->list_history_since: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **datetime**|  | [optional] 
 **event_type** | [**EpisodeHistoryEventType**](.md)|  | [optional] 
 **include_series** | **bool**|  | [optional] [default to False]
 **include_episode** | **bool**|  | [optional] [default to False]

### Return type

[**List[HistoryResource]**](HistoryResource.md)

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

