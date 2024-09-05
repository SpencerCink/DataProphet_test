This code encodes a date-time string and returns the shift label that applies to it. 
The shift hours played a pivotal role in the encoded labels. The assumptions that were made about this were as follows:
•	If the time period fell between a shift, for example between the times of 7:00:00 and 15:00:00, the code would be associated with the label A.

•	However, since the final shift was from 23:00:00 until 7:00:00, at the time of 7:00:00 would also fall within the category of C. 

•	Because of this, the category of the strong would be considered to be in C if the time value was exactly 7:00:00 and in A if the time was anything greater than this i.e. 7:00:01 etc. This structure was repeated for the rest of the categories and times. 

The months were directly read from a list using the values of the months as the increments of the list position, and the associated years and days values were directly taken from the date-time string. 
