
try:
    file_name = input("请输入要打开的文件名")
    f = open(file_name)
    for each in f:
        print(each)
except (OSError,TypeError) as reason:
    print("没有找到文件"+str(reason))
finally:
    print("+++++++++++++++")

