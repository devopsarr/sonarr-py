# sonarr.NamingConfigApi

All URIs are relative to *http://localhost:8989*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_naming_config**](NamingConfigApi.md#get_naming_config) | **GET** /api/v3/config/naming | 
[**get_naming_config_by_id**](NamingConfigApi.md#get_naming_config_by_id) | **GET** /api/v3/config/naming/{id} | 
[**get_naming_config_examples**](NamingConfigApi.md#get_naming_config_examples) | **GET** /api/v3/config/naming/examples | 
[**update_naming_config**](NamingConfigApi.md#update_naming_config) | **PUT** /api/v3/config/naming/{id} | 


# **get_naming_config**
> NamingConfigResource get_naming_config()



### Example

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
    api_instance = sonarr.NamingConfigApi(api_client)

    try:
        api_response = api_instance.get_naming_config()
        print("The response of NamingConfigApi->get_naming_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamingConfigApi->get_naming_config: %s\n" % e)
```

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
    api_instance = sonarr.NamingConfigApi(api_client)

    try:
        api_response = api_instance.get_naming_config()
        print("The response of NamingConfigApi->get_naming_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamingConfigApi->get_naming_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NamingConfigResource**](NamingConfigResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_naming_config_by_id**
> NamingConfigResource get_naming_config_by_id(id)



### Example

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
    api_instance = sonarr.NamingConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_naming_config_by_id(id)
        print("The response of NamingConfigApi->get_naming_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamingConfigApi->get_naming_config_by_id: %s\n" % e)
```

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
    api_instance = sonarr.NamingConfigApi(api_client)
    id = 56 # int | 

    try:
        api_response = api_instance.get_naming_config_by_id(id)
        print("The response of NamingConfigApi->get_naming_config_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamingConfigApi->get_naming_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**NamingConfigResource**](NamingConfigResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_naming_config_examples**
> get_naming_config_examples(rename_episodes=rename_episodes, replace_illegal_characters=replace_illegal_characters, multi_episode_style=multi_episode_style, standard_episode_format=standard_episode_format, daily_episode_format=daily_episode_format, anime_episode_format=anime_episode_format, series_folder_format=series_folder_format, season_folder_format=season_folder_format, specials_folder_format=specials_folder_format, include_series_title=include_series_title, include_episode_title=include_episode_title, include_quality=include_quality, replace_spaces=replace_spaces, separator=separator, number_style=number_style, id=id, resource_name=resource_name)



### Example

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
    api_instance = sonarr.NamingConfigApi(api_client)
    rename_episodes = True # bool |  (optional)
    replace_illegal_characters = True # bool |  (optional)
    multi_episode_style = 56 # int |  (optional)
    standard_episode_format = 'standard_episode_format_example' # str |  (optional)
    daily_episode_format = 'daily_episode_format_example' # str |  (optional)
    anime_episode_format = 'anime_episode_format_example' # str |  (optional)
    series_folder_format = 'series_folder_format_example' # str |  (optional)
    season_folder_format = 'season_folder_format_example' # str |  (optional)
    specials_folder_format = 'specials_folder_format_example' # str |  (optional)
    include_series_title = True # bool |  (optional)
    include_episode_title = True # bool |  (optional)
    include_quality = True # bool |  (optional)
    replace_spaces = True # bool |  (optional)
    separator = 'separator_example' # str |  (optional)
    number_style = 'number_style_example' # str |  (optional)
    id = 56 # int |  (optional)
    resource_name = 'resource_name_example' # str |  (optional)

    try:
        api_instance.get_naming_config_examples(rename_episodes=rename_episodes, replace_illegal_characters=replace_illegal_characters, multi_episode_style=multi_episode_style, standard_episode_format=standard_episode_format, daily_episode_format=daily_episode_format, anime_episode_format=anime_episode_format, series_folder_format=series_folder_format, season_folder_format=season_folder_format, specials_folder_format=specials_folder_format, include_series_title=include_series_title, include_episode_title=include_episode_title, include_quality=include_quality, replace_spaces=replace_spaces, separator=separator, number_style=number_style, id=id, resource_name=resource_name)
    except Exception as e:
        print("Exception when calling NamingConfigApi->get_naming_config_examples: %s\n" % e)
```

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
    api_instance = sonarr.NamingConfigApi(api_client)
    rename_episodes = True # bool |  (optional)
    replace_illegal_characters = True # bool |  (optional)
    multi_episode_style = 56 # int |  (optional)
    standard_episode_format = 'standard_episode_format_example' # str |  (optional)
    daily_episode_format = 'daily_episode_format_example' # str |  (optional)
    anime_episode_format = 'anime_episode_format_example' # str |  (optional)
    series_folder_format = 'series_folder_format_example' # str |  (optional)
    season_folder_format = 'season_folder_format_example' # str |  (optional)
    specials_folder_format = 'specials_folder_format_example' # str |  (optional)
    include_series_title = True # bool |  (optional)
    include_episode_title = True # bool |  (optional)
    include_quality = True # bool |  (optional)
    replace_spaces = True # bool |  (optional)
    separator = 'separator_example' # str |  (optional)
    number_style = 'number_style_example' # str |  (optional)
    id = 56 # int |  (optional)
    resource_name = 'resource_name_example' # str |  (optional)

    try:
        api_instance.get_naming_config_examples(rename_episodes=rename_episodes, replace_illegal_characters=replace_illegal_characters, multi_episode_style=multi_episode_style, standard_episode_format=standard_episode_format, daily_episode_format=daily_episode_format, anime_episode_format=anime_episode_format, series_folder_format=series_folder_format, season_folder_format=season_folder_format, specials_folder_format=specials_folder_format, include_series_title=include_series_title, include_episode_title=include_episode_title, include_quality=include_quality, replace_spaces=replace_spaces, separator=separator, number_style=number_style, id=id, resource_name=resource_name)
    except Exception as e:
        print("Exception when calling NamingConfigApi->get_naming_config_examples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rename_episodes** | **bool**|  | [optional] 
 **replace_illegal_characters** | **bool**|  | [optional] 
 **multi_episode_style** | **int**|  | [optional] 
 **standard_episode_format** | **str**|  | [optional] 
 **daily_episode_format** | **str**|  | [optional] 
 **anime_episode_format** | **str**|  | [optional] 
 **series_folder_format** | **str**|  | [optional] 
 **season_folder_format** | **str**|  | [optional] 
 **specials_folder_format** | **str**|  | [optional] 
 **include_series_title** | **bool**|  | [optional] 
 **include_episode_title** | **bool**|  | [optional] 
 **include_quality** | **bool**|  | [optional] 
 **replace_spaces** | **bool**|  | [optional] 
 **separator** | **str**|  | [optional] 
 **number_style** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **resource_name** | **str**|  | [optional] 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_naming_config**
> NamingConfigResource update_naming_config(id, naming_config_resource=naming_config_resource)



### Example

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
    api_instance = sonarr.NamingConfigApi(api_client)
    id = 'id_example' # str | 
    naming_config_resource = sonarr.NamingConfigResource() # NamingConfigResource |  (optional)

    try:
        api_response = api_instance.update_naming_config(id, naming_config_resource=naming_config_resource)
        print("The response of NamingConfigApi->update_naming_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamingConfigApi->update_naming_config: %s\n" % e)
```

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
    api_instance = sonarr.NamingConfigApi(api_client)
    id = 'id_example' # str | 
    naming_config_resource = sonarr.NamingConfigResource() # NamingConfigResource |  (optional)

    try:
        api_response = api_instance.update_naming_config(id, naming_config_resource=naming_config_resource)
        print("The response of NamingConfigApi->update_naming_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NamingConfigApi->update_naming_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **naming_config_resource** | [**NamingConfigResource**](NamingConfigResource.md)|  | [optional] 

### Return type

[**NamingConfigResource**](NamingConfigResource.md)

### Authorization

[apikey](../README.md#apikey), [X-Api-Key](../README.md#X-Api-Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

