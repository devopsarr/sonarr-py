# Ratings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**votes** | **int** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from sonarr.models.ratings import Ratings

# TODO update the JSON string below
json = "{}"
# create an instance of Ratings from a JSON string
ratings_instance = Ratings.from_json(json)
# print the JSON string representation of the object
print Ratings.to_json()

# convert the object into a dict
ratings_dict = ratings_instance.to_dict()
# create an instance of Ratings from a dict
ratings_form_dict = ratings.from_dict(ratings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


