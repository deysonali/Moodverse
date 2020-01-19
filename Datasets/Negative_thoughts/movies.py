import itertools

# Get raw dialouge
lines = open(r'../cornell movie-dialogs corpus/movie_lines.txt', 'rb')
lines_str = str(lines.read())[2:]
lines.close()
split = [char.split("\\n") for char in lines_str.split("+++$+++")]
merged = list(itertools.chain(*split))

# Save just dialogue
dialouge = []
c = 0
while c+4 < len(merged)-1:
        movie = merged[c+2].replace(" ", "")
        char = merged[c+1].replace(" ", "")
        text = merged[c+4]
        line = merged[c].replace(" ", "")
        dialouge.append(text)
        c+=5

keywords_i = ["I", "my", "me", "My"]
