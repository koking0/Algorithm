## Ideas

链表结构的经典题目。

不过我不想用经典方法做，哎，就是皮。

我把链表元素都拷贝到数组中，然后对数组排序，之后再把排完序之后的值赋回去。

[](./images/格局打开.jpg)

骚的一批。

## Code

### Python

```python
class Solution:
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		nums = []
		node = head
		while node:
			nums.append(node.val)
			node = node.next
		nums.sort()
		node = head
		for _, v in enumerate(nums):
			node.val = v
			node = node.next
		return head
```