# NamingConfigResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**rename_episodes** | **bool** |  | [optional] 
**replace_illegal_characters** | **bool** |  | [optional] 
**colon_replacement_format** | **int** |  | [optional] 
**multi_episode_style** | **int** |  | [optional] 
**standard_episode_format** | **str** |  | [optional] 
**daily_episode_format** | **str** |  | [optional] 
**anime_episode_format** | **str** |  | [optional] 
**series_folder_format** | **str** |  | [optional] 
**season_folder_format** | **str** |  | [optional] 
**specials_folder_format** | **str** |  | [optional] 
**include_series_title** | **bool** |  | [optional] 
**include_episode_title** | **bool** |  | [optional] 
**include_quality** | **bool** |  | [optional] 
**replace_spaces** | **bool** |  | [optional] 
**separator** | **str** |  | [optional] 
**number_style** | **str** |  | [optional] 

## Example

```python
from sonarr.models.naming_config_resource import NamingConfigResource

# TODO update the JSON string below
json = "{}"
# create an instance of NamingConfigResource from a JSON string
naming_config_resource_instance = NamingConfigResource.from_json(json)
# print the JSON string representation of the object
print NamingConfigResource.to_json()

# convert the object into a dict
naming_config_resource_dict = naming_config_resource_instance.to_dict()
# create an instance of NamingConfigResource from a dict
naming_config_resource_form_dict = naming_config_resource.from_dict(naming_config_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


