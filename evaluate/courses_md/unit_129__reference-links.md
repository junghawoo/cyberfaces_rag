---
title: "Reference links"
unit_id: 129
course_id: 0
level: "Foundation"
slug: reference-links
is_course: 0
---

# Reference links

**Description:** Check these out! gfdsg

## Text content

### Pellentesque ornare sem
Maecenas sed diam eget risus varius blandit sit amet non magna. Donec id elit non mi porta gravida at eget metus. Aenean eu leo quam. Pellentesque ornare sem lacinia ~~quam venenatis~~ vestibulum. Nulla vitae elit libero, a pharetra augue. **Donec sed odio dui**. Integer posuere erat a ante venenatis dapibus posuere velit aliquet. Nulla vitae elit libero, a pharetra augue. foo.

## Fetched resources (external URLs)

### Exercise (notebook)
*URL:* https://github.com/nujwoo/python101/05csv.ipynb

```python
import csv

with open('data/dummy.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
```
