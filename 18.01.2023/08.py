def read_details():
  f1 = open("./files/file8in.txt", "r")
  lines = f1.read()
  f1.close()
  return lines.split("\n")


def write_details(details):
  f1 = open("./files/file8in.txt", "w")
  f1.write(details)
  f1.close()

def add_record(staff_member):
  details = read_details()
  details.append(staff_member)
  write_details("\n".join(details))

def update_record():
  details = read_details()
  person_id = input("Enter id:")

  flag = False

  for i, x in enumerate(details):
    current_record = x.split("\t\t")
    if current_record[0] == person_id:
      print("1. Name")
      print("2. Number")
      c = int(input("Which attribute do you want to change?: "))

      if(c == 1):
        name = input("Enter new name: ")
        new_record = f"{current_record[0]}\t\t{name}\t\t{current_record[2]}"
        details[i] = new_record

      elif(c == 2):
        number = input("Enter new number: ")
        new_record = f"{current_record[0]}\t\t{current_record[1]}\t\t{number}"
        details[i] = new_record
    else:
      flag = True

  if(flag):
    print("No record found for id: ", person_id)
  else:
    print("Updated")
      

  write_details("\n".join(details))


def delete_record():

  details = read_details()
  person_id = input("Enter id:")

  flag = False

  for i, x in enumerate(details):
    current_record = x.split("\t\t")
    if current_record[0] == person_id:
      details.pop(i)
      flag = False
    else:
      flag = True

  if(flag):
    print("No record found for id: ", person_id)
  else:
    print("Deleted")
  write_details("\n".join(details))


def main():

  while(True):
    print("==============================================================")
    print("\t\tTELEPHONE DIRECTORY")

    print("1. Add a new record")
    print("2. Update a record")
    print("3. Delete a record")
    print("4. Print all the records")
    print("5. Display a particular record")

    print("-1. To exit")

    print("==============================================================")

    choice = int(input("Enter choice: "))
    print("")
    if(choice == -1):
      break

    elif choice ==1:
      staff_id = input("Enter id: ")
      staff_name = input("Enter name: ")
      staff_number = input("Enter number: ")

      staff_member = f"{staff_id}\t\t{staff_name}\t\t{staff_number}"
      add_record(staff_member)

    elif choice == 2:
      update_record()
    elif choice == 3:
      delete_record()
    elif choice == 4:
      print("ID\t\tNAME\t\tNUMBER")
      for member in read_details():
        print(member)
    elif choice == 5:
      _id = input("Enter id: ")
      for x in read_details():
        if(x.split("\t\t")[0] == _id):
          print("ID\t\tNAME\t\tNUMBER")
          print(x)
      


if __name__ == "__main__":
  main()