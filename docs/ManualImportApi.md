# sonarr.ManualImportApi

All URIs are relative to *http://localhost:8989*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manualimport**](ManualImportApi.md#create_manualimport) | **POST** /api/v3/manualimport | 
[**list_manualimport**](ManualImportApi.md#list_manualimport) | **GET** /api/v3/manualimport | 


# **create_manualimport**
> create_manualimport(manual_import_reprocess_resource=manual_import_reprocess_resource)



### Example

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with sonarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sonarr.ManualImportApi(api_client)
    manual_import_reprocess_resource = [sonarr.ManualImportReprocessResource()] # List[ManualImportReprocessResource] |  (optional)

    try:
        api_instance.create_manualimport(manual_import_reprocess_resource=manual_import_reprocess_resource)
    except Exception as e:
        print("Exception when calling ManualImportApi->create_manualimport: %s\n" % e)
```

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with sonarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sonarr.ManualImportApi(api_client)
    manual_import_reprocess_resource = [sonarr.ManualImportReprocessResource()] # List[ManualImportReprocessResource] |  (optional)

    try:
        api_instance.create_manualimport(manual_import_reprocess_resource=manual_import_reprocess_resource)
    except Exception as e:
        print("Exception when calling ManualImportApi->create_manualimport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manual_import_reprocess_resource** | [**List[ManualImportReprocessResource]**](ManualImportReprocessResource.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_manualimport**
> List[ManualImportResource] list_manualimport(folder=folder, download_id=download_id, series_id=series_id, season_number=season_number, filter_existing_files=filter_existing_files)



### Example

* Api Key Authentication (X-Api-Key):
```python
from __future__ import print_function
import time
import os
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with sonarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sonarr.ManualImportApi(api_client)
    folder = 'folder_example' # str |  (optional)
    download_id = 'download_id_example' # str |  (optional)
    series_id = 56 # int |  (optional)
    season_number = 56 # int |  (optional)
    filter_existing_files = True # bool |  (optional) (default to True)

    try:
        api_response = api_instance.list_manualimport(folder=folder, download_id=download_id, series_id=series_id, season_number=season_number, filter_existing_files=filter_existing_files)
        print("The response of ManualImportApi->list_manualimport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualImportApi->list_manualimport: %s\n" % e)
```

* Api Key Authentication (apikey):
```python
from __future__ import print_function
import time
import os
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

# Configure API key authorization: X-Api-Key
configuration.api_key['X-Api-Key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# Configure API key authorization: apikey
configuration.api_key['apikey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikey'] = 'Bearer'

# Enter a context with an instance of the API client
with sonarr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sonarr.ManualImportApi(api_client)
    folder = 'folder_example' # str |  (optional)
    download_id = 'download_id_example' # str |  (optional)
    series_id = 56 # int |  (optional)
    season_number = 56 # int |  (optional)
    filter_existing_files = True # bool |  (optional) (default to True)

    try:
        api_response = api_instance.list_manualimport(folder=folder, download_id=download_id, series_id=series_id, season_number=season_number, filter_existing_files=filter_existing_files)
        print("The response of ManualImportApi->list_manualimport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManualImportApi->list_manualimport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**|  | [optional] 
 **download_id** | **str**|  | [optional] 
 **series_id** | **int**|  | [optional] 
 **season_number** | **int**|  | [optional] 
 **filter_existing_files** | **bool**|  | [optional] [default to True]

### Return type

[**List[ManualImportResource]**](ManualImportResource.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
