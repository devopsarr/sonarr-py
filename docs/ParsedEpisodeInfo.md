# ParsedEpisodeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_title** | **str** |  | [optional] 
**series_title** | **str** |  | [optional] 
**series_title_info** | [**SeriesTitleInfo**](SeriesTitleInfo.md) |  | [optional] 
**quality** | [**QualityModel**](QualityModel.md) |  | [optional] 
**season_number** | **int** |  | [optional] 
**episode_numbers** | **List[int]** |  | [optional] 
**absolute_episode_numbers** | **List[int]** |  | [optional] 
**special_absolute_episode_numbers** | **List[float]** |  | [optional] 
**air_date** | **str** |  | [optional] 
**languages** | [**List[Language]**](Language.md) |  | [optional] 
**full_season** | **bool** |  | [optional] 
**is_partial_season** | **bool** |  | [optional] 
**is_multi_season** | **bool** |  | [optional] 
**is_season_extra** | **bool** |  | [optional] 
**is_split_episode** | **bool** |  | [optional] 
**special** | **bool** |  | [optional] 
**release_group** | **str** |  | [optional] 
**release_hash** | **str** |  | [optional] 
**season_part** | **int** |  | [optional] 
**release_tokens** | **str** |  | [optional] 
**daily_part** | **int** |  | [optional] 
**is_daily** | **bool** |  | [optional] [readonly] 
**is_absolute_numbering** | **bool** |  | [optional] [readonly] 
**is_possible_special_episode** | **bool** |  | [optional] [readonly] 
**is_possible_scene_season_special** | **bool** |  | [optional] [readonly] 

## Example

```python
from sonarr.models.parsed_episode_info import ParsedEpisodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ParsedEpisodeInfo from a JSON string
parsed_episode_info_instance = ParsedEpisodeInfo.from_json(json)
# print the JSON string representation of the object
print ParsedEpisodeInfo.to_json()

# convert the object into a dict
parsed_episode_info_dict = parsed_episode_info_instance.to_dict()
# create an instance of ParsedEpisodeInfo from a dict
parsed_episode_info_form_dict = parsed_episode_info.from_dict(parsed_episode_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


