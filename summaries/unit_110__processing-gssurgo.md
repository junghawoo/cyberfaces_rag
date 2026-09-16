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

## Summarized attachments

- **Jupyter Notebook Exercise** (`https://github.com/nujwoo/python101/05csv.ipynb`, notebook): GitHub Jupyter notebook demonstrating CSV file reading in Python using the csv module. Covers importing csv library, opening CSV files with custom delimiters and quote characters, creating csv.reader objects, and iterating through rows to print formatted output.
