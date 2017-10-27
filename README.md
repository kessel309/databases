Gist Database
===============

Today's project will combine our work with the [requests library](http://docs.python-requests.org/en/master/) and iterator usage with a new topic, databases. We will use requests to interface with Github's API to retrieve [gists](https://help.github.com/articles/about-gists/) and store them in a database that we will then be able to perform searches on. 

## The Importer
Your `import_gists_to_database` function will take three parameters:

 - `db`: The database object to connect to
 - `username`: The GitHub user whose gists we are going to retrieve
 - `commit` *(Optional, defaults to `True`)*: If `True`, automatically commit changes to database

You are going to use the [GitHub gists API](https://developer.github.com/v3/gists/) to retrieve the gists of a given user, insert those gists into a database (schema may be found in the `schema.sql` file), and if `commit` is True, commit those changes to the database.

## The Searcher
Your `search_gists` method should take a `db_connection` parameter (the database connection), as well as a variable number of keyword arguments to use in the search. This function should ultimately return an iterator that pumps out Gist objects with all the appropriate data filled in. These are the various keyword arguments your function should accept:

 - `github_id`
 - `public`
 - `created_at__gt`
 - `created_at__gte`
 - `created_at__lt`
 - `created_at__lte`
 - `updated_at__gt`
 - `updated_at__gte`
 - `updated_at__lt`
 - `updated_at__lte`
 - `comments`

**Datetime query parameters:** The keyword arguments starting with `created` and `updated` will be operating such that they will be comparing against the `created_at` and `updated_at` fields using the corresponding comparison:`gt` means greater than, `gte` greater than or equal tho, `lt` less than, `lte` less than or equal to
When comparing dates in your sql statements use the format `datetime(attribute) operator datetime(comparing_date)`

*Remember, the search should return an iterator that pumps out `Gist` objects (`Gist` definition is in `models.py`)*

