# SeasonStatisticsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_airing** | **datetime** |  | [optional] 
**previous_airing** | **datetime** |  | [optional] 
**episode_file_count** | **int** |  | [optional] 
**episode_count** | **int** |  | [optional] 
**total_episode_count** | **int** |  | [optional] 
**size_on_disk** | **int** |  | [optional] 
**release_groups** | **List[str]** |  | [optional] 
**percent_of_episodes** | **float** |  | [optional] [readonly] 

## Example

```python
from sonarr.models.season_statistics_resource import SeasonStatisticsResource

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonStatisticsResource from a JSON string
season_statistics_resource_instance = SeasonStatisticsResource.from_json(json)
# print the JSON string representation of the object
print(SeasonStatisticsResource.to_json())

# convert the object into a dict
season_statistics_resource_dict = season_statistics_resource_instance.to_dict()
# create an instance of SeasonStatisticsResource from a dict
season_statistics_resource_from_dict = SeasonStatisticsResource.from_dict(season_statistics_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


