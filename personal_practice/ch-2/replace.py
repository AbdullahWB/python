textEmail = """

Hello,
\t|<Name>| 
\tYou are selected for this job;
\tThanks
|<Date>|

"""

textEmail = textEmail.replace("|<Name>|", "John").replace("|<Date>|", "01-01-2026")

print(textEmail)