import re

def rmQM(line:str):
    res = line.replace("\",", "")
    i = res.find("\"")
    res = res[:i] + res[i+1:]
    return res

def rmScript(line : str):
    pattern = r"<.*?>"                  # 匹配"<"和">"之间的任意字符（非贪婪模式）
    res = re.sub(pattern, "", line)     # 使用re.sub()函数替换匹配到的子串为空字符串
    return res


def script2sql(script : str):
    res = ""

    for line in script.split("\n"):
        line = rmQM(line)
        line = rmScript(line)
        res = res + line + "\n"

    res = res[:-2]
    return res

def sql2script(sql : str):
    sqlArr = sql.split("\n")
    print(sqlArr)
    res = ""
    for line in sqlArr:
        s = 0
        e = 0
        for i in range(len(line)):
            if line[i] not in ["\t", " "]:
                s = i
                break
        k = len(line)-1
        while k >= 0:
            if line[k] not in ["\t", "\n", " "]:
                e = k
                break
        b = False
        line = line[s:e+1]
        for c in line:
            if c not in [' ', '\t', '\n']:
                b = True
                break
        if b:
            res += "\"" + line + "\"," + "\n"
    return res[:-2]



if __name__ == '__main__':
    f = open("./scripts/mbScript.txt", 'r')
    res = script2sql(f.read())
    print(res)