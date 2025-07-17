import csv
from modulees import validemail
validemails = []

with open("emails.csv",newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames
    for row in reader:
        Email = row.get("Email","").strip()
        if validemail(Email):
            validemails.append(row)
            print(validemails)
with open("validmails.csv", "w", newline= "")as file:
    writer = csv.writer(file)
    writer.writerow([validemails])
    validmails = list(filter(validemail, validemails))
    for email in validmails:
        writer.writerow(["emails"])
print(f"{len(validemails)} valid emails saved to 'validmails.csv'")



import csv
from modulees import emails_domain
emails = []
with open("validmails.csv", "r", newline= "")as file:
    reader = csv.DictReader(file)
    for row in reader:
        emails.append(row["Email"])
    emails_domain(emails)
