---
title: "Processing gSSURGO data to create soil dataset for a study area"
unit_id: 110
course_id: 4
level: "Expert"
slug: processing-gssurgo
is_course: 0
---

# Processing gSSURGO data to create soil dataset for a study area

## Fetched resources (external URLs)

### Jupyter Notebook Exercise (notebook)
*URL:* https://github.com/nujwoo/python101/05csv.ipynb

```python
import csv

with open('data/dummy.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
```
