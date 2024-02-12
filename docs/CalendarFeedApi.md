# sonarr.CalendarFeedApi

All URIs are relative to *http://localhost:8989*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_feed_v3_calendar_sonarr_ics**](CalendarFeedApi.md#get_feed_v3_calendar_sonarr_ics) | **GET** /feed/v3/calendar/sonarr.ics | 


# **get_feed_v3_calendar_sonarr_ics**
> get_feed_v3_calendar_sonarr_ics(past_days=past_days, future_days=future_days, tags=tags, unmonitored=unmonitored, premieres_only=premieres_only, as_all_day=as_all_day)



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
    api_instance = sonarr.CalendarFeedApi(api_client)
    past_days = 7 # int |  (optional) (default to 7)
    future_days = 28 # int |  (optional) (default to 28)
    tags = '' # str |  (optional) (default to '')
    unmonitored = False # bool |  (optional) (default to False)
    premieres_only = False # bool |  (optional) (default to False)
    as_all_day = False # bool |  (optional) (default to False)

    try:
        api_instance.get_feed_v3_calendar_sonarr_ics(past_days=past_days, future_days=future_days, tags=tags, unmonitored=unmonitored, premieres_only=premieres_only, as_all_day=as_all_day)
    except Exception as e:
        print("Exception when calling CalendarFeedApi->get_feed_v3_calendar_sonarr_ics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **past_days** | **int**|  | [optional] [default to 7]
 **future_days** | **int**|  | [optional] [default to 28]
 **tags** | **str**|  | [optional] [default to &#39;&#39;]
 **unmonitored** | **bool**|  | [optional] [default to False]
 **premieres_only** | **bool**|  | [optional] [default to False]
 **as_all_day** | **bool**|  | [optional] [default to False]

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
**2XX** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

