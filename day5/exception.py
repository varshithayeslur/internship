try:
    line_count = 0
    word_count = 0
    with open("data.txt") as f:
        lines = f.readlines()
        line_count = len(lines)
        for line in lines:
            word_count += len(line.split(" "))
            print(line, end= " ")
    print(f"\n line count is {line_count} and word count is {word_count}")

except Exception as e:
    print(f"file doesnot exist")