

import argparse
from lxml import etree

# Set up the Matt POST node
authorroot = etree.Element("author")
mattsfirst = etree.SubElement(authorroot, "first")
mattsfirst.text = "Matt"
mattslast = etree.SubElement(authorroot, "last")
mattslast.text = "POST"

# set up the parsing of arguments
parser = argparse.ArgumentParser()
parser.add_argument("xmlfiles", nargs='+', help="List of XML files")
args = parser.parse_args()
xmlfile = args.xmlfiles

# makes sure there are two authors for every paper, as per the task
for singlefile in args.xmlfiles:
    maintree = etree.parse(singlefile)
    mainroot = maintree.getroot()
    
    for paper in maintree.iter("paper"):
        paperid = paper.attrib
        
        numberofauthors = len(paper.findall("author"))
        if numberofauthors == 1:
            paper.insert(1, authorroot)
        else:
            for badauthors in paper.findall("author")[2:]:
                paper.remove(badauthors)

    #uppercase lastnames
    for lastname in paper.iter("last"):
        lastname.text = lastname.text.upper()
                    
        

    f = open(singlefile, "wb")
    maintree.write(f)
    f.close()
