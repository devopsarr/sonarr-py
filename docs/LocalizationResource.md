# LocalizationResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**strings** | **Dict[str, str]** |  | [optional] 

## Example

```python
from sonarr.models.localization_resource import LocalizationResource

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizationResource from a JSON string
localization_resource_instance = LocalizationResource.from_json(json)
# print the JSON string representation of the object
print LocalizationResource.to_json()

# convert the object into a dict
localization_resource_dict = localization_resource_instance.to_dict()
# create an instance of LocalizationResource from a dict
localization_resource_form_dict = localization_resource.from_dict(localization_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


