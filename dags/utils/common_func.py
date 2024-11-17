def regist(name, sex, *args, **kwargs):
    print(f"이름: {name}")
    print(f"성별: {sex}")
    print(f"기타옵션들: {args}")
    email = kwargs["email"] or "empty"
    phone = kwargs["phone"] or "empty"
    if email:
        print(email)
    if phone:
        print(phone)
