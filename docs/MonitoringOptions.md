# MonitoringOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_episodes_with_files** | **bool** |  | [optional] 
**ignore_episodes_without_files** | **bool** |  | [optional] 
**monitor** | [**MonitorTypes**](MonitorTypes.md) |  | [optional] 

## Example

```python
from sonarr.models.monitoring_options import MonitoringOptions

# TODO update the JSON string below
json = "{}"
# create an instance of MonitoringOptions from a JSON string
monitoring_options_instance = MonitoringOptions.from_json(json)
# print the JSON string representation of the object
print(MonitoringOptions.to_json())

# convert the object into a dict
monitoring_options_dict = monitoring_options_instance.to_dict()
# create an instance of MonitoringOptions from a dict
monitoring_options_from_dict = MonitoringOptions.from_dict(monitoring_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


