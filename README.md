CSV to XML
==========

Quickly convert a CSV file which has nested data into an XML file.

Usage
-----

```
python csvtoxml.py <3d-columns> < input.csv > output.xml
```

Where `<3d-columns>` is a comma-separated list of field names whose values
are themselves comma-separated lists (thus representing a nested set of data
within a row). For each sub-value in the column, a new XML tag will be
generated matching the column name.
