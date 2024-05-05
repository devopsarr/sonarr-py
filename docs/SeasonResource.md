# SeasonResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_number** | **int** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**statistics** | [**SeasonStatisticsResource**](SeasonStatisticsResource.md) |  | [optional] 
**images** | [**List[MediaCover]**](MediaCover.md) |  | [optional] 

## Example

```python
from sonarr.models.season_resource import SeasonResource

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonResource from a JSON string
season_resource_instance = SeasonResource.from_json(json)
# print the JSON string representation of the object
print(SeasonResource.to_json())

# convert the object into a dict
season_resource_dict = season_resource_instance.to_dict()
# create an instance of SeasonResource from a dict
season_resource_from_dict = SeasonResource.from_dict(season_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


