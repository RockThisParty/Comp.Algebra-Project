def html(filename, dictionary):
    with open(filename+".html", "w") as f:
        for line in filename:
            for i in dictionary:       
                f.write("Hello it's work")

