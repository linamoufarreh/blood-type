donor = input("Enter donor's blood type: ")
recipient = input("Enter recipient's blood type: ")

valids="A+A-B+B-O+O-AB-AB+"
if donor in valids and recipient in valids:
   if len(donor)==1 or len(recipient)==1:
      print("Invalid")
   elif len(donor)>=4 or len(recipient)>=4:
      print("Invalid")
   elif len(donor)==2 or len(recipient)==2:
       if "+" not in donor and "+" not in recipient:
           print("Invalid")
       elif "-" not in donor and "-" not in recipient:
           print("Invalid")
   elif donor== "O-" :
            print("Compatible")
   elif donor=="O+":
            if "+" in recipient:
                 print("Compatible")
            else:
                 print("Incompatible")
   elif donor=="B-":
            if "B" in recipient:
                 print("Compatible")
            else:
                 print("Incompatible")
   elif donor=="B+":
            if "B+" in recipient or "AB+" in recipient:
                 print("Compatible")
            else:
                 print("Incompatible")
   elif donor=="A-":
            if "A" in recipient:
                 print("Compatible")
            else:
                 print("Incompatible")
   elif donor=="A+":
            if "A+" in recipient or "AB+" in recipient :
                 print("Compatible")
            else:
                 print("Incompatible")
   elif donor=="AB-":
            if "AB" in recipient:
                 print("Compatible")
            else:
                 print("Incompatible")
   elif donor=="AB+":
            if recipient=="AB+":
                print("Compatible")
            else:
                print("Incompatible")
else:
    print("Invalid")
