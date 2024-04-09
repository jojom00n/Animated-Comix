from bs4 import *

class htmlparcing:
    def parse(self, comixproject):
        # load the file
        with open("existing_file.html") as inf:
            txt = inf.read()
            soup = bs4.BeautifulSoup(txt)

        # create new link
        new_link = soup.new_tag("link", rel="icon", type="image/png", href="img/tor.png")
        # insert it into the document
        soup.head.append(new_link)

        # save the file again
        with open("existing_file.html", "w") as outf:
            outf.write(str(soup))


