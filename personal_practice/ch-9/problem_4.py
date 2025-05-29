stringWord = """
I used to have a donkey,
One day I rode too fast.
When I spilled my coffee,
He called me an ass.

Oh no!
Oh no!

I used to have a money,
As naughty as could be.
One day when I woke up,
My monkey, he spanked me!

Oh no!
(Oh YES!)
On no!
La La La...

Drinking at the Hofbrau,
My waiter was a lout
I said I wanted schnitzel,
Not some sour Kraut.

Oh no!
(Oh mein schnizel!)
(Nein! Nein! 8, 7, 6, 5, 4, 3, Nein!)
Oh no!

Had a monkey robot soldier
Living inside my head.
So I took some wormwood.
Tried to kill him dead!

Oh no!
Oh no.
La la la...

I triedsta go whale spotting
On my new Ski Do,
But then I ran aground.
Ski Don't for me and you!

Oh no!
(Look out for the whales!)
Oh no!
La la la...

To get the freshest sausages
I had to get there first,
But when I got them all home,
Them brats, they were the worst!

Oh no!
Oh no.
La la la...

I used to have a donkey,
One day I rode too fast
When I spilled my coffee,
He called me an ass.

La la la...
Donkey!
"""

word = "donkey"
replacement = "#####"

# Step 1: Read the content of the file
with open("newFile.txt", "r") as f:
    content = f.read()  # Read entire file content

# Step 2: Replace occurrences of "donkey" (case insensitive)
content = content.replace(word, replacement).replace(word.capitalize(), replacement)

# Step 3: Write the modified content back to the file
with open("newFile.txt", "w") as f:
    f.write(content)

print("All occurrences of 'donkey' have been replaced with '#####'.")