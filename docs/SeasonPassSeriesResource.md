# SeasonPassSeriesResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**seasons** | [**List[SeasonResource]**](SeasonResource.md) |  | [optional] 

## Example

```python
from sonarr.models.season_pass_series_resource import SeasonPassSeriesResource

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonPassSeriesResource from a JSON string
season_pass_series_resource_instance = SeasonPassSeriesResource.from_json(json)
# print the JSON string representation of the object
print(SeasonPassSeriesResource.to_json())

# convert the object into a dict
season_pass_series_resource_dict = season_pass_series_resource_instance.to_dict()
# create an instance of SeasonPassSeriesResource from a dict
season_pass_series_resource_from_dict = SeasonPassSeriesResource.from_dict(season_pass_series_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


