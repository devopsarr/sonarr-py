# ReleaseEpisodeResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**season_number** | **int** |  | [optional] 
**episode_number** | **int** |  | [optional] 
**absolute_episode_number** | **int** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from sonarr.models.release_episode_resource import ReleaseEpisodeResource

# TODO update the JSON string below
json = "{}"
# create an instance of ReleaseEpisodeResource from a JSON string
release_episode_resource_instance = ReleaseEpisodeResource.from_json(json)
# print the JSON string representation of the object
print(ReleaseEpisodeResource.to_json())

# convert the object into a dict
release_episode_resource_dict = release_episode_resource_instance.to_dict()
# create an instance of ReleaseEpisodeResource from a dict
release_episode_resource_from_dict = ReleaseEpisodeResource.from_dict(release_episode_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


