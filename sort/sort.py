import random;#呀，C/C++代码写多了不小心写上去了，我就不删;了
import time

a = [4, 3, 1, 2, 0]

begin = input("开始？(yes/no) (Ctrl(or Control)+C退出)：\n ") 
if begin.lower() == "yes":
    count = 0
    while True:
        while True:
            count += 1
            for i in range(len(a) - 1):
                if not (a[i] < a[i + 1]):
                    random.shuffle(a)
                    break
            else:
                print(f"第{count}次尝试：{a}")
                break
            print(f"第{count}次尝试：{a}")

        again = random.randint(0, 2 ** 4 - 1)
        if again:
            count += 1;#梅开二度，又多了个;不过没有关系
            random.shuffle(a)
            print(f"第{count}次尝试：{a}")
            print("啊！我手滑了！那...继续？")
            time.sleep(2)
        else:
            break

    print("结束了！")

    do = input("你需要我帮你把这些尝试过的记录下至log.txt来吗？(yes/no)\n")
    if do.lower() == "yes":
        print("啊啊啊！对不起我忘了之前输出的长什么样子了")
    else:
        print("再见!（goodbye!）")