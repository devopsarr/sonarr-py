# SeriesTitleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**title_without_year** | **str** |  | [optional] 
**year** | **int** |  | [optional] 
**all_titles** | **List[str]** |  | [optional] 

## Example

```python
from sonarr.models.series_title_info import SeriesTitleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SeriesTitleInfo from a JSON string
series_title_info_instance = SeriesTitleInfo.from_json(json)
# print the JSON string representation of the object
print SeriesTitleInfo.to_json()

# convert the object into a dict
series_title_info_dict = series_title_info_instance.to_dict()
# create an instance of SeriesTitleInfo from a dict
series_title_info_form_dict = series_title_info.from_dict(series_title_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


