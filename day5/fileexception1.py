try:
    with open("data.txt") as fin, open("u_data.txt", "w") as fout:
        lines = fin.readlines()
        lines = [l.upper() for l in lines]      
        fout.writelines(lines)
except Exception as e:
    print(f"File not found please check path {e}")
    