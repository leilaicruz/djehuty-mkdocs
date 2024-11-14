# Application Programming Interface

The application programming interface (API) provided by d͡jehuty allows
for automating tasks otherwise done through the user interface. In
addition to automation, the API can also be used to gather additional
information, like statistics on Git repositories.

Throughout this chapter we provide examples for using the API using c͡url
and j͡q. Another way of seeing the API in action is to use the developer
tools in a web browser while performing the desired action using the web
user interface.

## The /͡v2 public interface

The v͡2 API was designed by Figshare[^1]. d͡jehuty implements a
backward-compatible version of it, with the following differences:

1.  The i͡d property is superseded by the u͡uid property.

2.  Error handling is done through precise HTTP error codes, rather than
    always returning 4͡00 on a usage error.

Unless specified otherwise, the HTTP C͡ontent-Type to interact with the
API is a͡pplication/json. In the case an API call returns information,
don’t forget to set the HTTP A͡ccept header appropriately.

### /͡v2/articles (HTTP )

The following parameters can be used:

|                 |              |                                                                                                          |
|:----------------|:-------------|:---------------------------------------------------------------------------------------------------------|
| **Parameter**   | **Required** | **Description**                                                                                          |
| o͡rder           | Optional     | Field to use for sorting.                                                                                |
| o͡rder_direction | Optional     | Can be either or .                                                                                       |
| i͡nstitution     | Optional     | The institution identifier to filter on.                                                                 |
| p͡ublished_since | Optional     | When set, datasets published before this timestamp are dropped from the results.                         |
| m͡odified_since  | Optional     | When set, only datasets modified after this timestamp are shown from the results.                        |
| g͡roup           | Optional     | The group identifier to filter on.                                                                       |
| r͡esource_doi    | Optional     | The DOI of the associated journal publication. When set, only returns datasets associated with this DOI. |
| i͡tem_type       | Optional     | Either for datasets or for software.                                                                     |
| d͡oi             | Optional     | The DOI of the dataset to search for.                                                                    |
| h͡andle          | Optional     | Unused.                                                                                                  |
| p͡age            | Optional     | The page number used in combination with p͡age_size.                                                      |
| p͡age_size       | Optional     | The number of datasets per page. Used in combination with p͡age.                                          |
| l͡imit           | Optional     | The maximum number of datasets to output. Used together with o͡ffset.                                     |
| o͡ffset          | Optional     | The number of datasets to skip in the output. Used together with l͡imit.                                  |

Example usage:

``` bash
curl "(@*\djehutybaseurl{}*@)/v2/articles?limit=100&published_since=2024-07-25" | jq
```

Output of the example:

``` JSON
[ /* Example output has been shortened. */
  {
    "id": null,
    "uuid": "4f8a9423-83fc-4263-9bb7-2aa83d73865d",
    "title": "Measurement data of a Low Speed Field Test of Tractor Se...",
    "doi": "10.4121/4f8a9423-83fc-4263-9bb7-2aa83d73865d.v1",
    "handle": null,
    "url": "(@*\djehutybaseurl{}*@)/v2/articles/4f8a...865d",
    "published_date": "2024-07-26T10:39:57",
    "thumb": null,
    "defined_type": 3,
    "defined_type_name": "dataset",
    "group_id": 28589,
    "url_private_api": "(@*\djehutybaseurl{}*@)/v2/account/articles/4f8a...865d",
    "url_public_api": "(@*\djehutybaseurl{}*@)/v2/articles/4f8a...865d",
    "url_private_html": "(@*\djehutybaseurl{}*@)/my/datasets/4f8a...865d/edit",
    "url_public_html": "(@*\djehutybaseurl{}*@)/datasets/4f8a...865d/1",
    ...
  }
]
```

### /͡v2/articles/search (HTTP )

In addition to the parameters of section , the following parameters can
be used.

|               |              |                          |
|:--------------|:-------------|:-------------------------|
| **Parameter** | **Required** | **Description**          |
| s͡earch_for    | Optional     | The terms to search for. |

Example usage:

``` bash
curl --request POST\
     --header "Content-Type: application/json"\
     --data '{ "search_for": "djehuty" }'\
     (@*\djehutybaseurl{}*@)/v2/articles/search | jq
```

Output of the example:

``` JSON
[ /* Example output has been shortened. */
  {
    "id": null,
    "uuid": "342efadc-66f8-4e9b-9d27-da7b28b849d2",
    "title": "Source code of the 4TU.ResearchData repository",
    "doi": "10.4121/342efadc-66f8-4e9b-9d27-da7b28b849d2.v1",
    "handle": null,
    "url": "(@*\djehutybaseurl{}*@)/v2/articles/342e...49d2",
    "published_date": "2023-03-20T11:29:10",
    "thumb": null,
    "defined_type": 9,
    "defined_type_name": "software",
    "group_id": 28586,
    "url_private_api": "(@*\djehutybaseurl{}*@)/v2/account/articles/342e...49d2",
    "url_public_api": "(@*\djehutybaseurl{}*@)/v2/articles/342e...49d2",
    "url_private_html": "(@*\djehutybaseurl{}*@)/my/datasets/342e...49d2/edit",
    "url_public_html": "(@*\djehutybaseurl{}*@)/datasets/342e...49d2/1",
    ...
  }
]
```

### /͡v2/articles/\<dataset-id\> (HTTP )

Example usage:

``` bash
curl (@*\djehutybaseurl{}*@)/v2/articles/342efadc-66f8-4e9b-9d27-da7b28b849d2 | jq
```

Output of the example:

``` JSON
{ /* Example output has been shortened. */
  "files": ...,
  "custom_fields": ...,
  "authors": ...,
  "description": "<p>This dataset contains the source code of the 4TU...",
  "license": ...,
  "tags": ...,
  "categories": ...,
  "references": ...,
  "id": null,
  "uuid": "342efadc-66f8-4e9b-9d27-da7b28b849d2",
  "title": "Source code of the 4TU.ResearchData repository",
  "doi": "10.4121/342efadc-66f8-4e9b-9d27-da7b28b849d2.v1",
  "url": "(@*\djehutybaseurl{}*@)/v2/articles/342e...49d2",
  "published_date": "2023-03-20T11:29:10",
  "timeline": ...,
  ...
}
```

### /͡v2/articles/\<dataset-id\>/versions (HTTP )

Example usage:

``` bash
curl (@*\djehutybaseurl{}*@)/v2/articles/342efadc-66f8-4e9b-9d27-da7b28b849d2/versions | jq
```

Output of the example:

``` JSON
[
  {
    "version": 1,
    "url": "(@*\djehutybaseurl{}*@)/v2/articles/342efadc-66f8-4e9b-9d27-da7b28b849d2/versions/1"
  }
]
```

### /͡v2/articles/\<dataset-id\>/versions/\<version\> (HTTP )

Example usage:

``` bash
curl (@*\djehutybaseurl{}*@)/v2/articles/342efadc-66f8-4e9b-9d27-da7b28b849d2/versions/1 | jq
```

The output of the example is identical to the example output of section
.

### /͡v2/articles/\<dataset-id\>/versions/\<version\>/embargo (HTTP )

Example usage:

``` bash
curl (@*\djehutybaseurl{}*@)/v2/articles/c1274889-b797-43bd-a3b1-ee0611d58fd7/versions/2/embargo | jq
```

Output of the example:

``` JSON
{
  "is_embargoed": true,
  "embargo_date": "2039-06-30",
  "embargo_type": "article",
  "embargo_title": "Under embargo",
  "embargo_reason": "<p>Need consent to publish the data</p>",
  "embargo_options": []
}
```

### /͡v2/articles/\<dataset-id\>/files (HTTP )

Example usage:

``` bash
curl (@*\djehutybaseurl{}*@)/v2/articles/342efadc-66f8-4e9b-9d27-da7b28b849d2/files
```

Output of the example:

``` JSON
[ /* Example output has been shortened. */
  {
    "id": null,
    "uuid": "d3e1c325-7fa9-4cb9-884e-0b9cd2059292",
    "name": "djehuty-0.0.1.tar.gz",
    "size": 3713709,
    "is_link_only": false,
    "is_incomplete": false,
    "download_url": "(@*\djehutybaseurl{}*@)/file/342e...49d2/d3e1...9292",
    "supplied_md5": null,
    "computed_md5": "910e9b0f79a0af548f59b3d8a56c3bf4"
  }
]
```

### /͡v2/articles/\<dataset-id\>/files/\<file-id\> (HTTP )

Example usage:

``` bash
curl (@*\djehutybaseurl{}*@)/v2/articles/342e...49d2/files/d3e1...9292 | jq
```

Output of the example:

``` JSON
{ /* Example output has been shortened. */
  "id": null,
  "uuid": "d3e1c325-7fa9-4cb9-884e-0b9cd2059292",
  "name": "djehuty-0.0.1.tar.gz",
  "size": 3713709,
  "is_link_only": false,
  "is_incomplete": false,
  "download_url": "(@*\djehutybaseurl{}*@)/file/342e...49d2/d3e1...9292",
  "supplied_md5": null,
  "computed_md5": "910e9b0f79a0af548f59b3d8a56c3bf4"
}
```

### /͡v2/collections (HTTP )

The following parameters can be used:

|                 |              |                                                                                                             |
|:----------------|:-------------|:------------------------------------------------------------------------------------------------------------|
| **Parameter**   | **Required** | **Description**                                                                                             |
| o͡rder           | Optional     | Field to use for sorting.                                                                                   |
| o͡rder_direction | Optional     | Can be either or .                                                                                          |
| i͡nstitution     | Optional     | The institution identifier to filter on.                                                                    |
| p͡ublished_since | Optional     | When set, collections published before this timestamp are dropped from the results.                         |
| m͡odified_since  | Optional     | When set, only collections modified after this timestamp are shown from the results.                        |
| g͡roup           | Optional     | The group identifier to filter on.                                                                          |
| r͡esource_doi    | Optional     | The DOI of the associated journal publication. When set, only returns collections associated with this DOI. |
| d͡oi             | Optional     | The DOI of the collection to search for.                                                                    |
| h͡andle          | Optional     | Unused.                                                                                                     |
| p͡age            | Optional     | The page number used in combination with p͡age_size.                                                         |
| p͡age_size       | Optional     | The number of collections per page. Used in combination with p͡age.                                          |
| l͡imit           | Optional     | The maximum number of collections to output. Used together with o͡ffset.                                     |
| o͡ffset          | Optional     | The number of collections to skip in the output. Used together with l͡imit.                                  |

Example usage:

``` bash
curl "(@*\djehutybaseurl{}*@)/v2/collections?limit=100&published_since=2024-07-25" | jq
```

Output of the example:

``` JSON
[ /* Example output has been shortened. */
  {
    "id": null,
    "uuid": "0fe9ab80-6e6a-4087-a509-ce09dddfa3d9",
    "title": "PhD research 'Untangling the complexity of local water ...'",
    "doi": "10.4121/0fe9ab80-6e6a-4087-a509-ce09dddfa3d9.v1",
    "handle": "",
    "url": "(@*\djehutybaseurl{}*@)/v2/collections/0fe9...fa3d9",
    "timeline": {
      "posted": "2024-08-13T14:09:52",
      "firstOnline": "2024-08-13T14:09:51",
      ...
    },
    "published_date": "2024-08-13T14:09:52"
  },
  ...
]
```

### /͡v2/collections/search (HTTP )

In addition to the parameters of section , the following parameters can
be used.

|               |              |                          |
|:--------------|:-------------|:-------------------------|
| **Parameter** | **Required** | **Description**          |
| s͡earch_for    | Optional     | The terms to search for. |

Example usage:

``` bash
curl --request POST\
     --header "Content-Type: application/json"\
     --data '{ "search_for": "wingtips" }'\
     (@*\djehutybaseurl{}*@)/v2/collections/search | jq
```

Output of the example:

``` JSON
[  /* Example output has been shortened. */
  {
    "id": 6070238,
    "uuid": "3dfc4ef2-7f79-4d33-81a7-9c6ae09a2782",
    "title": "Flared Folding Wingtips - TU Delft",
    "doi": "10.4121/c.6070238.v1",
    "handle": "",
    "url": "(@*\djehutybaseurl{}*@)/v2/collections/3dfc...2782",
    "timeline": {
      "posted": "2023-04-05T15:05:04",
      "firstOnline": "2023-04-05T15:05:03",
      ...
    },
    "published_date": "2023-04-05T15:05:04"
  },
  ...
]
```

### /͡v2/collections/\<collection-id\> (HTTP )

Example usage:

``` bash
curl (@*\djehutybaseurl{}*@)/v2/collections/3dfc4ef2-7f79-4d33-81a7-9c6ae09a2782 | jq
```

Output of the example:

``` JSON
{ /* Example output has been shortened. */
  "version": 3,
  ...
  "description": "<p>This collection contains the results of the work ...",
  "categories": [ ... ],
  "references": [],
  "tags": [ ... ],
  "created_date": "2024-08-08T15:48:55",
  "modified_date": "2024-08-12T11:24:39",
  "id": 6070238,
  "uuid": "3dfc4ef2-7f79-4d33-81a7-9c6ae09a2782",
  "title": "Flared Folding Wingtips - TU Delft",
  "doi": "10.4121/c.6070238.v3",
  "published_date": "2024-08-12T11:24:40",
  "timeline": ...
  ...
}
```

### /͡v2/collections/\<collection-id\>/versions (HTTP )

Example usage:

``` bash
curl (@*\djehutybaseurl{}*@)/v2/collections/3dfc4ef2-7f79-4d33-81a7-9c6ae09a2782/versions | jq
```

Output of the example:

``` JSON
[ /* Example output has been shortened. */
  {
    "version": 3,
    "url": "(@*\djehutybaseurl{}*@)/v2/collections/3dfc...2782/versions/3"
  },
  {
    "version": 2,
    "url": "(@*\djehutybaseurl{}*@)/v2/collections/3dfc...2782/versions/2"
  },
  {
    "version": 1,
    "url": "(@*\djehutybaseurl{}*@)/v2/collections/3dfc...2782/versions/1"
  }
]
```

### /͡v2/collections/\<collection-id\>/versions/\<version\> (HTTP )

Example usage:

``` bash
curl (@*\djehutybaseurl{}*@)/v2/collections/3dfc4ef2-7f79-4d33-81a7-9c6ae09a2782/versions/2 | jq
```

Output of the example:

``` JSON
{ /* Example output has been shortened. */
  "version": 2,
  ...
  "description": "<p>This collection contains the results of the work ...",
  "categories": [ ... ],
  "references": [],
  "tags": [ ... ],
  "references": [],
  "tags": [ ... ],
  "authors": [ ... ],
  "created_date": "2023-04-05T15:07:35",
  "modified_date": "2023-05-26T15:19:11",
  "id": 6070238,
  "uuid": "3dfc4ef2-7f79-4d33-81a7-9c6ae09a2782",
  "title": "Flared Folding Wingtips - TU Delft",
  "doi": "10.4121/c.6070238.v2",
  ...
}
```

### /͡v2/categories (HTTP )

Each dataset and collection is categorized using a controlled vocabulary
of categories. This API endpoint provides those categories.

Example usage:

``` bash
curl (@*\djehutybaseurl{}*@)/v2/categories | jq
```

Output of the example:

``` JSON
[ /* Example output has been shortened. */
  {
    "id": 13622,
    "uuid": "01fddd41-68d2-4e28-9d9c-18347847e7d1",
    "title": "Mining and Extraction of Energy Resources",
    "parent_id": 13620,
    "parent_uuid": "6e5bdc69-96db-41e4-ac0b-18812b46c49c",
    "path": "",
    "source_id": null,
    "taxonomy_id": null
  },
  {
    "id": 13443,
    "uuid": "026f555c-2826-4a83-97ff-0f230fb54ddb",
    "title": "Livestock Raising",
    "parent_id": 13440,
    "parent_uuid": "45a8c849-ab59-4302-af79-09b8c0677df8",
    "path": "",
    "source_id": null,
    "taxonomy_id": null
  },
  ...
]
```

### /͡v2/licenses (HTTP )

Publishing a dataset involves communicating under which conditions it
can be re-used. The licenses under which you can publish a dataset can
be found with this API endpoint.

Example usage:

``` bash
curl (@*\djehutybaseurl{}*@)/v2/licenses | jq
```

Output of the example:

``` JSON
[ /* Example output has been shortened. */
  {
    "value": 1,
    "name": "CC BY 4.0",
    "url": "https://creativecommons.org/licenses/by/4.0/",
    "type": "data"
  },
  {
    "value": 10,
    "name": "CC BY-NC 4.0",
    "url": "https://creativecommons.org/licenses/by-nc/4.0/",
    "type": "data"
  },
  ...
]
```

## The /͡v2 private interface

The interaction with the v͡2 private interface API requires an API token.
Such a token can be obtained from the dashboard page after logging in.
This token can then be passed along in the A͡uthorization HTTP header as:

    Authorization: token YOUR_TOKEN_HERE

### /͡v2/account/articles (HTTP )

This API endpoint lists the draft datasets of the account to which the
authorization token belongs.

The following parameters can be used:

|               |              |                                                                         |
|:--------------|:-------------|:------------------------------------------------------------------------|
| **Parameter** | **Required** | **Description**                                                         |
| p͡age          | Optional     | The page number used in combination with p͡age_size.                     |
| p͡age_size     | Optional     | The number of datasets per page. Used in combination with p͡age.         |
| l͡imit         | Optional     | The maximum number of datasets to output. Used together with o͡ffset.    |
| o͡ffset        | Optional     | The number of datasets to skip in the output. Used together with l͡imit. |

Example usage:

``` bash
curl -H "Authorization: token YOUR_TOKEN_HERE" (@*\djehutybaseurl{}*@)/v2/account/articles | jq
```

Output of the example:

``` JSON
{ /* Example output has been shortened. */
  "id": null,
  "uuid": "6ddd7a31-8ad8-4c20-95a3-e68fe716fa42",
  "title": "Example draft dataset",
  "doi": null,
  "handle": null,
  "url": "(@*\djehutybaseurl{}*@)/v2/articles/6ddd7a31-8ad8-4c20-95a3-e68fe716fa42",
  "published_date": null,
  ...
}
```

### /͡v2/account/articles (HTTP )

This API endpoint can be used to create a new dataset.

The following parameters can be used:

|                |                         |                                                                                                                                                                                                                                    |
|:---------------|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Parameter**  | **Data type**           | **Description**                                                                                                                                                                                                                    |
| t͡itle          | s͡tring                  | The title of the dataset.                                                                                                                                                                                                          |
| d͡escription    | s͡tring                  | A description of the dataset.                                                                                                                                                                                                      |
| t͡ags           | list of s͡trings         | Keywords to enhance the findability of the dataset. Instead of using the key , you may also use the key .                                                                                                                          |
| r͡eferences     | list of s͡trings         | URLs to resources referring to this dataset, or resources that this dataset refers to.                                                                                                                                             |
| c͡ategories     | list of s͡trings         | Categories are a controlled vocabulary and can be used to make the dataset findable in the categorical overviews. The s͡tring values expected here can be found under the property with a call to . For more details, see section . |
| a͡uthors        | list of author records  |                                                                                                                                                                                                                                    |
| d͡efined_type   | s͡tring                  | One of: f͡igure, o͡nline resource, p͡reprint, b͡ook, c͡onference contribution, m͡edia, d͡ataset, p͡oster, j͡ournal contribution, p͡resentation, t͡hesis or s͡oftware.                                                                          |
| f͡unding        | s͡tring                  | One-liner to cite funding.                                                                                                                                                                                                         |
| f͡unding_list   | list of funding records |                                                                                                                                                                                                                                    |
| l͡icense        | i͡nteger                 | Licences communicate under which conditions the dataset can be re-used. The i͡nteger value to submit here can be found as the v͡alue property in a call to . For more details, see section .                                         |
| d͡oi            | s͡tring                  | Do not use this field as a DOI will be automatically assigned upon publication..                                                                                                                                                   |
| h͡andle         | s͡tring                  | Do not use this field as it is deprecated.                                                                                                                                                                                         |
| r͡esource_doi   | s͡tring                  | The URL of the DOI of an associated peer-reviewed journal publication.                                                                                                                                                             |
| r͡esource_title | s͡tring                  | The title of the associated peer-reviewed journal publication.                                                                                                                                                                     |
| p͡ublisher      | s͡tring                  | The name of the data repository publishing the dataset.                                                                                                                                                                            |
| c͡ustom_fields  | list of key-value pairs |                                                                                                                                                                                                                                    |
| t͡imeline       |                         | Do not use this field because it will be automatically populated during the publication process.                                                                                                                                   |

[^1]:
