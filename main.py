import re
posts=[("User1","This is a bad post with a toxic attitude check http://news.com"),
       ("User2","This is a good post. please visit http://youtube.com"),
       ("User3","I hate maths but i love science check http://science.com"),
       ("User4", "Virtusa is a global provider of business tranformation and It services visit http://virtusa.com")]
banned_words=["bad","toxic","hate"]
cleaned=[]
blocked_count=0
links=[]
flags={}
def extract_links(t:str)->list[str]:
    return [w for w in t.split() if w.startswith("http")]
def mask_banned_words(t:str,banned:list[str])-> tuple[str,int]:
    c=0
    for i in banned:
        pat=re.compile(re.escape(i),re.IGNORECASE)
        count=len(pat.findall(t))
        if count:
            t=pat.sub("***",t)
            c+=count
    return t,c
for name,text in posts:
    if name not in flags:
        flags[name]=0
    links_in_curr=extract_links(text)
    links.append(links_in_curr)
    cleaned_curr,count=mask_banned_words(text,banned_words)
    status="clean"
    if count>0:
        flags[name]+=count
        blocked_count+=1
        status="Blocked"
    cleaned.append((name,cleaned_curr))
    print(f"name:{name}, status: {status}, post: {cleaned_curr}")
links_path="links_found.txt"
with open(links_path,mode="w") as file:
    for link in links:
        for i in link:
            file.write(i+"\n")
print("Cleaned posts \n")
for i in cleaned:
    print(i)
print("\n")
print("Links found in posts \n")
for link in links:
    print(link)
print("\n")
print("Moderator flags \n")
for k,v in flags.items():
    print(f"{k}: {v}")
print("\n")
cleaned_count=sum(1 for _, t in cleaned if "***" in t)
print("Final report \n")
print(f"Total no of posts: {len(posts)} \n")
print(f"Total no of flagged posts: {blocked_count}\n")
print(f"Total no of cleaned posts: {cleaned_count}\n")





        