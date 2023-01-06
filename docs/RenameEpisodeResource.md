# RenameEpisodeResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**series_id** | **int** |  | [optional] 
**season_number** | **int** |  | [optional] 
**episode_numbers** | **List[int]** |  | [optional] 
**episode_file_id** | **int** |  | [optional] 
**existing_path** | **str** |  | [optional] 
**new_path** | **str** |  | [optional] 

## Example

```python
from sonarr.models.rename_episode_resource import RenameEpisodeResource

# TODO update the JSON string below
json = "{}"
# create an instance of RenameEpisodeResource from a JSON string
rename_episode_resource_instance = RenameEpisodeResource.from_json(json)
# print the JSON string representation of the object
print RenameEpisodeResource.to_json()

# convert the object into a dict
rename_episode_resource_dict = rename_episode_resource_instance.to_dict()
# create an instance of RenameEpisodeResource from a dict
rename_episode_resource_form_dict = rename_episode_resource.from_dict(rename_episode_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


