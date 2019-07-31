try:
    with open("story.txt") as f:
        lines = f.readlines()
        new_list = []
        for line in lines:
            line = line.replace('love','hate')
            new_list.append(line)
except Exception as e:
    print(f"file not found {e}")