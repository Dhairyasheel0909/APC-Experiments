story="""A boy is playing there. 
There is a playground. 
A plane is in the sky. 
The sky is pink. 
Main football ground is big
Alphabet and number are allowed in password."""

count=len(story.splitlines())
print("Total lines :",count)
for line in story.splitlines():
	if line.startswith("T"):
		count-=1
print("Number of lines Not start with T :",count)

	
	























