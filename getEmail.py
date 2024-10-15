def get_mail(name:str) -> str:
    words = name.split()
    email = ""
    for i in range(len(words)):
        if i == len(words) - 1:
            email += words[i].lower()
        else:
            email += words[i][:1].lower()
    return email

if __name__ == '__main__':
    fileName = open('input.txt', 'r')
    raw_data = fileName.readlines()
    email_list =  []
    count_list = list(range(len(raw_data)))
    for i in range(len(raw_data)):
        fullname = raw_data[i]
        fullname = fullname.strip()
        print(fullname)
        mail = get_mail(fullname)
        if mail not in email_list:
            email_list.append(mail)
            count_list[email_list.index(mail)] = 0
        else:
            email_list.append(mail+str(count_list[email_list.index(mail)]+1))
            count_list[email_list.index(mail)] += 1

    print(email_list)

