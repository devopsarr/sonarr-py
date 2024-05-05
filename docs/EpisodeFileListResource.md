# EpisodeFileListResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**episode_file_ids** | **List[int]** |  | [optional] 
**languages** | [**List[Language]**](Language.md) |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**scene_name** | **str** |  | [optional] 
**release_group** | **str** |  | [optional] 

## Example

```python
from sonarr.models.episode_file_list_resource import EpisodeFileListResource

# TODO update the JSON string below
json = "{}"
# create an instance of EpisodeFileListResource from a JSON string
episode_file_list_resource_instance = EpisodeFileListResource.from_json(json)
# print the JSON string representation of the object
print(EpisodeFileListResource.to_json())

# convert the object into a dict
episode_file_list_resource_dict = episode_file_list_resource_instance.to_dict()
# create an instance of EpisodeFileListResource from a dict
episode_file_list_resource_from_dict = EpisodeFileListResource.from_dict(episode_file_list_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


