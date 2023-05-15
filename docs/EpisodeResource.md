# EpisodeResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**series_id** | **int** |  | [optional] 
**tvdb_id** | **int** |  | [optional] 
**episode_file_id** | **int** |  | [optional] 
**season_number** | **int** |  | [optional] 
**episode_number** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**air_date** | **str** |  | [optional] 
**air_date_utc** | **datetime** |  | [optional] 
**overview** | **str** |  | [optional] 
**episode_file** | [**EpisodeFileResource**](EpisodeFileResource.md) |  | [optional] 
**has_file** | **bool** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**absolute_episode_number** | **int** |  | [optional] 
**scene_absolute_episode_number** | **int** |  | [optional] 
**scene_episode_number** | **int** |  | [optional] 
**scene_season_number** | **int** |  | [optional] 
**unverified_scene_numbering** | **bool** |  | [optional] 
**end_time** | **datetime** |  | [optional] 
**grab_date** | **datetime** |  | [optional] 
**series_title** | **str** |  | [optional] 
**series** | [**SeriesResource**](SeriesResource.md) |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**grabbed** | **bool** |  | [optional] 

## Example

```python
from sonarr.models.episode_resource import EpisodeResource

# TODO update the JSON string below
json = "{}"
# create an instance of EpisodeResource from a JSON string
episode_resource_instance = EpisodeResource.from_json(json)
# print the JSON string representation of the object
print EpisodeResource.to_json()

# convert the object into a dict
episode_resource_dict = episode_resource_instance.to_dict()
# create an instance of EpisodeResource from a dict
episode_resource_form_dict = episode_resource.from_dict(episode_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


