# SeriesResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**alternate_titles** | [**List[AlternateTitleResource]**](AlternateTitleResource.md) |  | [optional] 
**sort_title** | **str** |  | [optional] 
**status** | [**SeriesStatusType**](SeriesStatusType.md) |  | [optional] 
**ended** | **bool** |  | [optional] [readonly] 
**profile_name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**next_airing** | **datetime** |  | [optional] 
**previous_airing** | **datetime** |  | [optional] 
**network** | **str** |  | [optional] 
**air_time** | **str** |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 
**original_language** | [**Language**](Language.md) |  | [optional] 
**remote_poster** | **str** |  | [optional] 
**seasons** | [**List[SeasonResource]**](SeasonResource.md) |  | [optional] 
**year** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**season_folder** | **bool** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**use_scene_numbering** | **bool** |  | [optional] 
**runtime** | **int** |  | [optional] 
**tvdb_id** | **int** |  | [optional] 
**tv_rage_id** | **int** |  | [optional] 
**tv_maze_id** | **int** |  | [optional] 
**first_aired** | **datetime** |  | [optional] 
**last_aired** | **datetime** |  | [optional] 
**series_type** | [**SeriesTypes**](SeriesTypes.md) |  | [optional] 
**clean_title** | **str** |  | [optional] 
**imdb_id** | **str** |  | [optional] 
**title_slug** | **str** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**folder** | **str** |  | [optional] 
**certification** | **str** |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**added** | **datetime** |  | [optional] 
**add_options** | [**AddSeriesOptions**](AddSeriesOptions.md) |  | [optional] 
**ratings** | [**Ratings**](Ratings.md) |  | [optional] 
**statistics** | [**SeriesStatisticsResource**](SeriesStatisticsResource.md) |  | [optional] 
**episodes_changed** | **bool** |  | [optional] 
**language_profile_id** | **int** |  | [optional] [readonly] 

## Example

```python
from sonarr.models.series_resource import SeriesResource

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesResource from a JSON string
series_resource_instance = SeriesResource.from_json(json)
# print the JSON string representation of the object
print SeriesResource.to_json()

# convert the object into a dict
series_resource_dict = series_resource_instance.to_dict()
# create an instance of SeriesResource from a dict
series_resource_form_dict = series_resource.from_dict(series_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


