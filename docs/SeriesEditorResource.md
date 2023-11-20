# SeriesEditorResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**series_ids** | **List[int]** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**monitor_new_items** | [**NewItemMonitorTypes**](NewItemMonitorTypes.md) |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**series_type** | [**SeriesTypes**](SeriesTypes.md) |  | [optional] 
**season_folder** | **bool** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**apply_tags** | [**ApplyTags**](ApplyTags.md) |  | [optional] 
**move_files** | **bool** |  | [optional] 
**delete_files** | **bool** |  | [optional] 
**add_import_list_exclusion** | **bool** |  | [optional] 

## Example

```python
from sonarr.models.series_editor_resource import SeriesEditorResource

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesEditorResource from a JSON string
series_editor_resource_instance = SeriesEditorResource.from_json(json)
# print the JSON string representation of the object
print SeriesEditorResource.to_json()

# convert the object into a dict
series_editor_resource_dict = series_editor_resource_instance.to_dict()
# create an instance of SeriesEditorResource from a dict
series_editor_resource_form_dict = series_editor_resource.from_dict(series_editor_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


