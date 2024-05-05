# AddSeriesOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_episodes_with_files** | **bool** |  | [optional] 
**ignore_episodes_without_files** | **bool** |  | [optional] 
**monitor** | [**MonitorTypes**](MonitorTypes.md) |  | [optional] 
**search_for_missing_episodes** | **bool** |  | [optional] 
**search_for_cutoff_unmet_episodes** | **bool** |  | [optional] 

## Example

```python
from sonarr.models.add_series_options import AddSeriesOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AddSeriesOptions from a JSON string
add_series_options_instance = AddSeriesOptions.from_json(json)
# print the JSON string representation of the object
print(AddSeriesOptions.to_json())

# convert the object into a dict
add_series_options_dict = add_series_options_instance.to_dict()
# create an instance of AddSeriesOptions from a dict
add_series_options_from_dict = AddSeriesOptions.from_dict(add_series_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


