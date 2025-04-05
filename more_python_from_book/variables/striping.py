full_name = "Mohammad Abdullah "
print(full_name,len(full_name))
new_full_name = full_name.rstrip()
print("pre",full_name,len(new_full_name),"new",new_full_name) #this for right


another_full_name = " python"
print(another_full_name,len(another_full_name))
new_another_full_name = another_full_name.lstrip()
print("pre",another_full_name,len(new_another_full_name),"new",new_another_full_name) #this for left


more_full_name = " python "
print(more_full_name,len(more_full_name))
new_more_full_name = more_full_name.strip()
print("pre",more_full_name,len(new_more_full_name),"new",new_more_full_name) #this for both sides