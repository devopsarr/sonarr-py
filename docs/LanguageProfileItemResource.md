# LanguageProfileItemResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**allowed** | **bool** |  | [optional] 

## Example

```python
from sonarr.models.language_profile_item_resource import LanguageProfileItemResource

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageProfileItemResource from a JSON string
language_profile_item_resource_instance = LanguageProfileItemResource.from_json(json)
# print the JSON string representation of the object
print(LanguageProfileItemResource.to_json())

# convert the object into a dict
language_profile_item_resource_dict = language_profile_item_resource_instance.to_dict()
# create an instance of LanguageProfileItemResource from a dict
language_profile_item_resource_from_dict = LanguageProfileItemResource.from_dict(language_profile_item_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


