# sonarr.MediaManagementConfigApi

All URIs are relative to *http://localhost:8989*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_mediamanagement**](MediaManagementConfigApi.md#get_config_mediamanagement) | **GET** /api/v3/config/mediamanagement | 
[**get_config_mediamanagement_by_id**](MediaManagementConfigApi.md#get_config_mediamanagement_by_id) | **GET** /api/v3/config/mediamanagement/{id} | 
[**update_config_mediamanagement**](MediaManagementConfigApi.md#update_config_mediamanagement) | **PUT** /api/v3/config/mediamanagement/{id} | 


# **get_config_mediamanagement**
> MediaManagementConfigResource get_config_mediamanagement()



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
    api_instance = sonarr.MediaManagementConfigApi(api_client)

    try:
        api_response = api_instance.get_config_mediamanagement()
        print("The response of MediaManagementConfigApi->get_config_mediamanagement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaManagementConfigApi->get_config_mediamanagement: %s\n" % e)
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
    api_instance = sonarr.MediaManagementConfigApi(api_client)

    try:
        api_response = api_instance.get_config_mediamanagement()
        print("The response of MediaManagementConfigApi->get_config_mediamanagement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaManagementConfigApi->get_config_mediamanagement: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MediaManagementConfigResource**](MediaManagementConfigResource.md)

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

# **get_config_mediamanagement_by_id**
> MediaManagementConfigResource get_config_mediamanagement_by_id(id)



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
    api_instance = sonarr.MediaManagementConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_config_mediamanagement_by_id(id)
        print("The response of MediaManagementConfigApi->get_config_mediamanagement_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaManagementConfigApi->get_config_mediamanagement_by_id: %s\n" % e)
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
    api_instance = sonarr.MediaManagementConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_config_mediamanagement_by_id(id)
        print("The response of MediaManagementConfigApi->get_config_mediamanagement_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaManagementConfigApi->get_config_mediamanagement_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MediaManagementConfigResource**](MediaManagementConfigResource.md)

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

# **update_config_mediamanagement**
> MediaManagementConfigResource update_config_mediamanagement(id, media_management_config_resource=media_management_config_resource)



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
    api_instance = sonarr.MediaManagementConfigApi(api_client)
    id = 'id_example' # str | 
    media_management_config_resource = sonarr.MediaManagementConfigResource() # MediaManagementConfigResource |  (optional)

    try:
        api_response = api_instance.update_config_mediamanagement(id, media_management_config_resource=media_management_config_resource)
        print("The response of MediaManagementConfigApi->update_config_mediamanagement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaManagementConfigApi->update_config_mediamanagement: %s\n" % e)
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
    api_instance = sonarr.MediaManagementConfigApi(api_client)
    id = 'id_example' # str | 
    media_management_config_resource = sonarr.MediaManagementConfigResource() # MediaManagementConfigResource |  (optional)

    try:
        api_response = api_instance.update_config_mediamanagement(id, media_management_config_resource=media_management_config_resource)
        print("The response of MediaManagementConfigApi->update_config_mediamanagement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaManagementConfigApi->update_config_mediamanagement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **media_management_config_resource** | [**MediaManagementConfigResource**](MediaManagementConfigResource.md)|  | [optional] 

### Return type

[**MediaManagementConfigResource**](MediaManagementConfigResource.md)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
