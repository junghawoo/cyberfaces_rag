I want to count the unnecessary tokens in the data.jsonl file. Write a python script calculate the total number of words before and after cleaning. The cleaning rule is like this: inside quotation mark, split a sentence using seperators of empty character(blank). Treat colon as a valid word.  for example.,"FAIR Climate and Water Science: Introduction" will be split into FAIR Climiate and water science : Introduction. 


Writ a python program to count unnecessary tokens:[ quotation mark, comma, curly bracket ]. Here token is defined a word or colon. For example, this line has 18 of them:

{"id":1,"course_id":4,"parent_id":0,"level_id":1,"title":"FAIR Climate and Water Science: Introduction"}

The valid tokens in the example includes id : course_id : 4 parent_id : 0 level_id : 1 title : FAIR Climate and Water Science : Introduction. Ignore comma and do not count in as a valid token.

Can you write a python code doing that, and count the fraction of unwanted tokens out of the total number of tokens? 
