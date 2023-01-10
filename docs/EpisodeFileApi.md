# sonarr.EpisodeFileApi

All URIs are relative to *http://localhost:8989*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_episode_file**](EpisodeFileApi.md#delete_episode_file) | **DELETE** /api/v3/episodefile/{id} | 
[**delete_episode_file_bulk**](EpisodeFileApi.md#delete_episode_file_bulk) | **DELETE** /api/v3/episodefile/bulk | 
[**get_episode_file_by_id**](EpisodeFileApi.md#get_episode_file_by_id) | **GET** /api/v3/episodefile/{id} | 
[**list_episode_file**](EpisodeFileApi.md#list_episode_file) | **GET** /api/v3/episodefile | 
[**put_episode_file_bulk**](EpisodeFileApi.md#put_episode_file_bulk) | **PUT** /api/v3/episodefile/bulk | 
[**put_episode_file_editor**](EpisodeFileApi.md#put_episode_file_editor) | **PUT** /api/v3/episodefile/editor | 
[**update_episode_file**](EpisodeFileApi.md#update_episode_file) | **PUT** /api/v3/episodefile/{id} | 


# **delete_episode_file**
> delete_episode_file(id)



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
    api_instance = sonarr.EpisodeFileApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_episode_file(id)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->delete_episode_file: %s\n" % e)
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
    api_instance = sonarr.EpisodeFileApi(api_client)
    id = 56 # int | 

    try:
        api_instance.delete_episode_file(id)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->delete_episode_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[X-Api-Key](../README.md#X-Api-Key), [apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_episode_file_bulk**
> delete_episode_file_bulk(episode_file_list_resource=episode_file_list_resource)



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
    api_instance = sonarr.EpisodeFileApi(api_client)
    episode_file_list_resource = sonarr.EpisodeFileListResource() # EpisodeFileListResource |  (optional)

    try:
        api_instance.delete_episode_file_bulk(episode_file_list_resource=episode_file_list_resource)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->delete_episode_file_bulk: %s\n" % e)
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
    api_instance = sonarr.EpisodeFileApi(api_client)
    episode_file_list_resource = sonarr.EpisodeFileListResource() # EpisodeFileListResource |  (optional)

    try:
        api_instance.delete_episode_file_bulk(episode_file_list_resource=episode_file_list_resource)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->delete_episode_file_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_file_list_resource** | [**EpisodeFileListResource**](EpisodeFileListResource.md)|  | [optional] 

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

# **get_episode_file_by_id**
> EpisodeFileResource get_episode_file_by_id(id)



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
    api_instance = sonarr.EpisodeFileApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_episode_file_by_id(id)
        print("The response of EpisodeFileApi->get_episode_file_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->get_episode_file_by_id: %s\n" % e)
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
    api_instance = sonarr.EpisodeFileApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_episode_file_by_id(id)
        print("The response of EpisodeFileApi->get_episode_file_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->get_episode_file_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**EpisodeFileResource**](EpisodeFileResource.md)

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

# **list_episode_file**
> List[EpisodeFileResource] list_episode_file(series_id=series_id, episode_file_ids=episode_file_ids)



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
    api_instance = sonarr.EpisodeFileApi(api_client)
    series_id = 56 # int |  (optional)
    episode_file_ids = [56] # List[int] |  (optional)

    try:
        api_response = api_instance.list_episode_file(series_id=series_id, episode_file_ids=episode_file_ids)
        print("The response of EpisodeFileApi->list_episode_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->list_episode_file: %s\n" % e)
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
    api_instance = sonarr.EpisodeFileApi(api_client)
    series_id = 56 # int |  (optional)
    episode_file_ids = [56] # List[int] |  (optional)

    try:
        api_response = api_instance.list_episode_file(series_id=series_id, episode_file_ids=episode_file_ids)
        print("The response of EpisodeFileApi->list_episode_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->list_episode_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **int**|  | [optional] 
 **episode_file_ids** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**List[EpisodeFileResource]**](EpisodeFileResource.md)

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

# **put_episode_file_bulk**
> put_episode_file_bulk(episode_file_resource=episode_file_resource)



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
    api_instance = sonarr.EpisodeFileApi(api_client)
    episode_file_resource = [sonarr.EpisodeFileResource()] # List[EpisodeFileResource] |  (optional)

    try:
        api_instance.put_episode_file_bulk(episode_file_resource=episode_file_resource)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->put_episode_file_bulk: %s\n" % e)
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
    api_instance = sonarr.EpisodeFileApi(api_client)
    episode_file_resource = [sonarr.EpisodeFileResource()] # List[EpisodeFileResource] |  (optional)

    try:
        api_instance.put_episode_file_bulk(episode_file_resource=episode_file_resource)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->put_episode_file_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_file_resource** | [**List[EpisodeFileResource]**](EpisodeFileResource.md)|  | [optional] 

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

# **put_episode_file_editor**
> put_episode_file_editor(episode_file_list_resource=episode_file_list_resource)



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
    api_instance = sonarr.EpisodeFileApi(api_client)
    episode_file_list_resource = sonarr.EpisodeFileListResource() # EpisodeFileListResource |  (optional)

    try:
        api_instance.put_episode_file_editor(episode_file_list_resource=episode_file_list_resource)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->put_episode_file_editor: %s\n" % e)
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
    api_instance = sonarr.EpisodeFileApi(api_client)
    episode_file_list_resource = sonarr.EpisodeFileListResource() # EpisodeFileListResource |  (optional)

    try:
        api_instance.put_episode_file_editor(episode_file_list_resource=episode_file_list_resource)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->put_episode_file_editor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **episode_file_list_resource** | [**EpisodeFileListResource**](EpisodeFileListResource.md)|  | [optional] 

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

# **update_episode_file**
> EpisodeFileResource update_episode_file(id, episode_file_resource=episode_file_resource)



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
    api_instance = sonarr.EpisodeFileApi(api_client)
    id = 'id_example' # str | 
    episode_file_resource = sonarr.EpisodeFileResource() # EpisodeFileResource |  (optional)

    try:
        api_response = api_instance.update_episode_file(id, episode_file_resource=episode_file_resource)
        print("The response of EpisodeFileApi->update_episode_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->update_episode_file: %s\n" % e)
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
    api_instance = sonarr.EpisodeFileApi(api_client)
    id = 'id_example' # str | 
    episode_file_resource = sonarr.EpisodeFileResource() # EpisodeFileResource |  (optional)

    try:
        api_response = api_instance.update_episode_file(id, episode_file_resource=episode_file_resource)
        print("The response of EpisodeFileApi->update_episode_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EpisodeFileApi->update_episode_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **episode_file_resource** | [**EpisodeFileResource**](EpisodeFileResource.md)|  | [optional] 

### Return type

[**EpisodeFileResource**](EpisodeFileResource.md)

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

