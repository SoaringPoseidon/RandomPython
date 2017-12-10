#parsing and processing XML using DOM

import xml.dom.minidom

def main():
	doc = xml.dom.minidom.parse("seanwang.xml")
	print (doc.nodeName)
	print (doc.firstChild.tagName)


	fName = doc.getElementsByTagName("firstname")
	lName = doc.getElementsByTagName("lastname")
    
	skills = doc.getElementsByTagName("skill")
	num = len(skills)
	print (fName[0].firstChild._data + " " + lName[0].firstChild._data + " has " + str(num) + " skills")
	for skill in skills:
		print (skill.getAttribute("name"))

	newSkill = doc.createElement("skill")
	newSkill.setAttribute("name", "perl")
	doc.firstChild.appendChild(newSkill)

	skills = doc.getElementsByTagName("skill")
	num = len(skills)
	print (fName[0].firstChild._data + " " + lName[0].firstChild._data + " has " + str(num) + " skills")
	for skill in skills:
		print (skill.getAttribute("name"))

if __name__ == "__main__":
	main()