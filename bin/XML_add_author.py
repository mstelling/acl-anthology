# no comments, I'm tired af. hope this works

import argparse
from lxml import etree

authorroot = etree.Element("author")
mattsfirst = etree.SubElement(authorroot, "first")
mattsfirst.text = "Matt"
mattslast = etree.SubElement(authorroot, "last")
mattslast.text = "POST"


parser = argparse.ArgumentParser()
parser.add_argument("xmlfile", nargs='+', help="List of XML files")
args = parser.parse_args()
xmlfile = args.xmlfile

for singlefile in args.xmlfile:
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
                
            for lastname in paper.iter("last"):
                lastname.text = lastname.text.upper()
                    
        

    f = open(singlefile, "wb")
    maintree.write(f)
    f.close()
