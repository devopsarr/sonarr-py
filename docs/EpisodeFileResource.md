# EpisodeFileResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**series_id** | **int** |  | [optional] 
**season_number** | **int** |  | [optional] 
**relative_path** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**date_added** | **datetime** |  | [optional] 
**scene_name** | **str** |  | [optional] 
**release_group** | **str** |  | [optional] 
**languages** | [**List[Language]**](Language.md) |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**custom_formats** | [**List[CustomFormatResource]**](CustomFormatResource.md) |  | [optional] 
**custom_format_score** | **int** |  | [optional] 
**media_info** | [**MediaInfoResource**](MediaInfoResource.md) |  | [optional] 
**quality_cutoff_not_met** | **bool** |  | [optional] 

## Example

```python
from sonarr.models.episode_file_resource import EpisodeFileResource

# TODO update the JSON string below
json = "{}"
# create an instance of EpisodeFileResource from a JSON string
episode_file_resource_instance = EpisodeFileResource.from_json(json)
# print the JSON string representation of the object
print EpisodeFileResource.to_json()

# convert the object into a dict
episode_file_resource_dict = episode_file_resource_instance.to_dict()
# create an instance of EpisodeFileResource from a dict
episode_file_resource_form_dict = episode_file_resource.from_dict(episode_file_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


