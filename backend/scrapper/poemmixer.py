filename = "./artists_cleaned/poem/pukhraj/Copy.txt"

with open(filename, "r+", encoding="utf8") as file:
    # read all lines from the file
    lines = file.readlines()

    # remove the first two lines and the last three lines
    lines = lines[2:-3]

    # move the file pointer to the beginning of the file
    file.seek(0)

    # truncate the file
    file.truncate()

    # write the modified lines back to the file
    file.writelines(lines)

    # close the file
    file.close()
