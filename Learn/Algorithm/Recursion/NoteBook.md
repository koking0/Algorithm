T(N) = aT(N/b) + O(N<sup>d</sup>)

T(N):总样本量

a:子过程发生了多少次

T(N/b):子样本量

b:划分次数

O(N<sup>d</sup>):除子过程之外的时间复杂度

**1) log(b,a)>d -> 复杂度为O(N<sup>log(b,a)</sup>)**

**2) log(b,a)=d -> 复杂度为O(N<sup>d</sup>\*logN**

**3) log(b,a)<d -> 复杂度为O(N<sup>d</sup>)**