f = open("test.txt", "w")
f.write("Olá, meu nome é Iury!")
print(f.tell())
f.write("Tudo bem?")
f.writelines(["\neu gosto de ensinar", "\n Sou engenheiro de dados"])

with open("emails.txt", "r") as emails_file:
    with open("emails_copy.txt", "w") as emails_copy:
        emails_copy.write(emails_file.read())

with open("emails_copy.txt", "a") as file:
    print(file.tell())
    file.write("\ncontato@hotmart.com")