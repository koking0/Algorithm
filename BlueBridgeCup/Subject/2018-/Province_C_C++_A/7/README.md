﻿## 三体攻击

【题目描述】
三体人将对地球发起攻击。为了抵御攻击，地球人派出了 A×B×C 艘战舰，在太空中排成一个 A 层 B 行 C 列的立方体。其中，第 i 层第 j 行第 k 列的战舰（记为战舰 (i,j,k)）的生命值为 d(i,j,k)。

三体人将会对地球发起 m 轮“立方体攻击”，每次攻击会对一个小立方体中的所有战舰都造成相同的伤害。具体地，第 t 轮攻击用 7 个参数 lat,rat,lbt,rbt,lct,rct,ht 描述；
所有满足 i∈[lat,rat],j∈[lbt,rbt],k∈[lct,rct] 的战舰 (i,j,k) 会受到 ht 的伤害。如果一个战舰累计受到的总伤害超过其防御力，那么这个战舰会爆炸。

地球指挥官希望你能告诉他，第一艘爆炸的战舰是在哪一轮攻击后爆炸的。

【输入格式】
从标准输入读入数据。

第一行包括 4 个正整数 A,B,C,m；
第二行包含 A×B×C 个整数，其中第 ((i−1)×B+(j−1))×C+(k−1)+1 个数为 d(i,j,k)；
第 3 到第 m+2 行中，第 (t−2) 行包含 7 个正整数 lat,rat,lbt,rbt,lct,rct,ht。

【输出格式】
输出到标准输出。

输出第一个爆炸的战舰是在哪一轮攻击后爆炸的。保证一定存在这样的战舰。

【样例输入】
2 2 2 3
1 1 1 1 1 1 1 1
1 2 1 2 1 1 1
1 1 1 2 1 2 1
1 1 1 1 1 1 2

【样例输出】
2

【样例解释】
在第 2 轮攻击后，战舰 (1,1,1) 总共受到了 2 点伤害，超出其防御力导致爆炸。

【数据约定】
对于 10% 的数据，B=C=1；
对于 20% 的数据，C=1；
对于 40% 的数据，A×B×C,m≤10,000；
对于 70% 的数据，A,B,C≤200；
对于所有数据，A×B×C≤10^6,m≤10^6,0≤d(i,j,k),ht≤10^9。


资源约定：
峰值内存消耗（含虚拟机） < 256M
CPU消耗  < 2000ms


请严格按要求输出，不要画蛇添足地打印类似：“请您输入...” 的多余内容。

注意：
main函数需要返回0;
只使用ANSI C/ANSI C++ 标准;
不要调用依赖于编译环境或操作系统的特殊函数。
所有依赖的函数必须明确地在源文件中 #include <xxx>
不能通过工程设置而省略常用头文件。

提交程序时，注意选择所期望的语言类型和编译器类型。