def read_text():
    quotes = open(r"C:\Users\v.venkatakrishnan\Desktop\Workspace\Python\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
read_text()