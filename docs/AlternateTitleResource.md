# AlternateTitleResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**season_number** | **int** |  | [optional] 
**scene_season_number** | **int** |  | [optional] 
**scene_origin** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from sonarr.models.alternate_title_resource import AlternateTitleResource

# TODO update the JSON string below
json = "{}"
# create an instance of AlternateTitleResource from a JSON string
alternate_title_resource_instance = AlternateTitleResource.from_json(json)
# print the JSON string representation of the object
print(AlternateTitleResource.to_json())

# convert the object into a dict
alternate_title_resource_dict = alternate_title_resource_instance.to_dict()
# create an instance of AlternateTitleResource from a dict
alternate_title_resource_form_dict = alternate_title_resource.from_dict(alternate_title_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


