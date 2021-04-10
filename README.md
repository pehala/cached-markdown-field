# CachedMarkdownField for Django Models

This Field caches compiled Markdown and then uses the cached value when queried. This saves time spent compiling Markdown on every request.

## Example
```python
 class NameAndDescription(models.Model):
     name = CharField(max_length=20)
     description = CachedMarkdownField()

 instance = NameAndDescription()
 instance.description = "text"
 assert instance.description == "<p>text</p>"
```

## Settings
`CachedMarkdownField` recongnized two `SETTINGS.py` settings
```python
# Enables caching
MARKDOWN_CACHE = True

# If false, will raise error if not already compiled
MARKDOWN_CACHE_RUNTIME = True
```


## How does it work?

Internally `CachedMarkdownField` uses `CompositeField` and stores the cached value in separate field. `CachedMarkdownField` is a proxy and will add two fields into the actual model. In the example
above ``instance.description`` returns a proxy object that maps the fields ``markdown`` and ``cached``
to the model fields ``description_markdown`` and ``description_cached``.
