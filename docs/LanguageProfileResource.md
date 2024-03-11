# LanguageProfileResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**upgrade_allowed** | **bool** |  | [optional] 
**cutoff** | [**Language**](Language.md) |  | [optional] 
**languages** | [**List[LanguageProfileItemResource]**](LanguageProfileItemResource.md) |  | [optional] 

## Example

```python
from sonarr.models.language_profile_resource import LanguageProfileResource

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageProfileResource from a JSON string
language_profile_resource_instance = LanguageProfileResource.from_json(json)
# print the JSON string representation of the object
print(LanguageProfileResource.to_json())

# convert the object into a dict
language_profile_resource_dict = language_profile_resource_instance.to_dict()
# create an instance of LanguageProfileResource from a dict
language_profile_resource_form_dict = language_profile_resource.from_dict(language_profile_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


