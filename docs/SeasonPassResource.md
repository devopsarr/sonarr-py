# SeasonPassResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series** | [**List[SeasonPassSeriesResource]**](SeasonPassSeriesResource.md) |  | [optional] 
**monitoring_options** | [**MonitoringOptions**](MonitoringOptions.md) |  | [optional] 

## Example

```python
from sonarr.models.season_pass_resource import SeasonPassResource

# TODO update the JSON string below
json = "{}"
# create an instance of SeasonPassResource from a JSON string
season_pass_resource_instance = SeasonPassResource.from_json(json)
# print the JSON string representation of the object
print SeasonPassResource.to_json()

# convert the object into a dict
season_pass_resource_dict = season_pass_resource_instance.to_dict()
# create an instance of SeasonPassResource from a dict
season_pass_resource_form_dict = season_pass_resource.from_dict(season_pass_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


