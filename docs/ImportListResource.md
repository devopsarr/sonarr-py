# ImportListResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**fields** | [**List[ContractField]**](ContractField.md) |  | [optional] 
**implementation_name** | **str** |  | [optional] 
**implementation** | **str** |  | [optional] 
**config_contract** | **str** |  | [optional] 
**info_link** | **str** |  | [optional] 
**message** | [**ProviderMessage**](ProviderMessage.md) |  | [optional] 
**tags** | **List[int]** |  | [optional] 
**presets** | [**List[ImportListResource]**](ImportListResource.md) |  | [optional] 
**enable_automatic_add** | **bool** |  | [optional] 
**search_for_missing_episodes** | **bool** |  | [optional] 
**should_monitor** | [**MonitorTypes**](MonitorTypes.md) |  | [optional] 
**monitor_new_items** | [**NewItemMonitorTypes**](NewItemMonitorTypes.md) |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**quality_profile_id** | **int** |  | [optional] 
**series_type** | [**SeriesTypes**](SeriesTypes.md) |  | [optional] 
**season_folder** | **bool** |  | [optional] 
**list_type** | [**ImportListType**](ImportListType.md) |  | [optional] 
**list_order** | **int** |  | [optional] 
**min_refresh_interval** | **str** |  | [optional] 

## Example

```python
from sonarr.models.import_list_resource import ImportListResource

# TODO update the JSON string below
json = "{}"
# create an instance of ImportListResource from a JSON string
import_list_resource_instance = ImportListResource.from_json(json)
# print the JSON string representation of the object
print ImportListResource.to_json()

# convert the object into a dict
import_list_resource_dict = import_list_resource_instance.to_dict()
# create an instance of ImportListResource from a dict
import_list_resource_form_dict = import_list_resource.from_dict(import_list_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


