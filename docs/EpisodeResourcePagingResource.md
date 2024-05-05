# EpisodeResourcePagingResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**sort_key** | **str** |  | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 
**total_records** | **int** |  | [optional] 
**records** | [**List[EpisodeResource]**](EpisodeResource.md) |  | [optional] 

## Example

```python
from sonarr.models.episode_resource_paging_resource import EpisodeResourcePagingResource

# TODO update the JSON string below
json = "{}"
# create an instance of EpisodeResourcePagingResource from a JSON string
episode_resource_paging_resource_instance = EpisodeResourcePagingResource.from_json(json)
# print the JSON string representation of the object
print(EpisodeResourcePagingResource.to_json())

# convert the object into a dict
episode_resource_paging_resource_dict = episode_resource_paging_resource_instance.to_dict()
# create an instance of EpisodeResourcePagingResource from a dict
episode_resource_paging_resource_from_dict = EpisodeResourcePagingResource.from_dict(episode_resource_paging_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


