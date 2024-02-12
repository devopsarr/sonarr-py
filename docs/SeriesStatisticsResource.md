# SeriesStatisticsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_count** | **int** |  | [optional] 
**episode_file_count** | **int** |  | [optional] 
**episode_count** | **int** |  | [optional] 
**total_episode_count** | **int** |  | [optional] 
**size_on_disk** | **int** |  | [optional] 
**release_groups** | **List[str]** |  | [optional] 
**percent_of_episodes** | **float** |  | [optional] [readonly] 

## Example

```python
from sonarr.models.series_statistics_resource import SeriesStatisticsResource

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesStatisticsResource from a JSON string
series_statistics_resource_instance = SeriesStatisticsResource.from_json(json)
# print the JSON string representation of the object
print SeriesStatisticsResource.to_json()

# convert the object into a dict
series_statistics_resource_dict = series_statistics_resource_instance.to_dict()
# create an instance of SeriesStatisticsResource from a dict
series_statistics_resource_form_dict = series_statistics_resource.from_dict(series_statistics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


