# EpisodesMonitoredResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**episode_ids** | **List[int]** |  | [optional] 
**monitored** | **bool** |  | [optional] 

## Example

```python
from sonarr.models.episodes_monitored_resource import EpisodesMonitoredResource

# TODO update the JSON string below
json = "{}"
# create an instance of EpisodesMonitoredResource from a JSON string
episodes_monitored_resource_instance = EpisodesMonitoredResource.from_json(json)
# print the JSON string representation of the object
print(EpisodesMonitoredResource.to_json())

# convert the object into a dict
episodes_monitored_resource_dict = episodes_monitored_resource_instance.to_dict()
# create an instance of EpisodesMonitoredResource from a dict
episodes_monitored_resource_form_dict = episodes_monitored_resource.from_dict(episodes_monitored_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


