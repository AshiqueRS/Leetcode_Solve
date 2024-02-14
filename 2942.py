words = ["leet","code"]
x = "e"
st = []
for i in range(len(words)):
    if x in words[i]:
        st.append(i)
print(st) 