# this is first time attemps at coding challenges - not the best code 


# REVERSE INTEGER

def reverse(x):
    INT_MAX = 2147483647
    print(INT_MAX)
    INT_MIN = 2147483648
    num = x   
    is_negative = False
    if x == 0:
        return 0
    if x < 0:
        num = abs(num)
        is_negative = True

    num_list = []
    while num:       
        num_list.append(num % 10)
        num = num // 10
    print(num_list)

    new_num = 0
    for i in range(0, len(num_list)):
        print('num {} x {}'.format(num_list[i], (10 ** (len(num_list) - i - 1))))
        if new_num/10 > INT_MAX / 10 or \
            (new_num/10  == INT_MAX / 10 and num_list[i] > 7):
            print('got int max - new num {}'.format(new_num))
            return 0
        if is_negative:
            if new_num/10  > INT_MIN / 10 or \
                (new_num/10  == INT_MIN / 10 and num_list[i] > 8):
                print('got int min')
                return 0
        new_num += num_list[i] * (10 ** (len(num_list) - i - 1))

    if is_negative:
        new_num = -new_num

    print(new_num)
    return new_num

print(reverse(123))
print(reverse(-123))
print(reverse(-2147483412))

def reverse2(x):
    INT_MAX = 2147483647       
    INT_MIN = 2147483648
    rev = 0
    is_negative = x < 0
    x = abs(x)
    
    while x != 0:
        pop = x % 10
        x //= 10
        if rev > INT_MAX/10 or (rev == INT_MAX / 10 and pop > 7):
            print('got int max - REV {}'.format(rev))
            return 0
        if rev > INT_MIN/10 or (rev == INT_MIN / 10 and pop > 8):
            print('got int min')
            return 0
        rev = rev * 10 + pop
    if is_negative:
        rev = -rev

    return rev
print('REVERSE 2')
print(reverse2(123))
print(reverse2(-123))
print(reverse2(-2147483412))

# PALINDROM NUMBER
# string conversion method
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    
    num_str = str(x)

    for i in range(0, len(num_str)//2):
        print(num_str[i])
        print('compare {} to {}'.format(num_str[i], num_str[len(num_str) - 1 - i]))
        if num_str[i] != num_str[len(num_str) - 1 - i] :
            return False
    return True

print(isPalindrome(12121))
print(isPalindrome(1221))
print(isPalindrome(123421))

print('Pali 2')

def isPalindrome2(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    rev_num = 0
    while x > rev_num:
        rev_num = rev_num * 10 + x % 10
        x //= 10

    return x == rev_num or x == rev_num//10

print(isPalindrome2(12121))
print(isPalindrome2(1221))
print(isPalindrome2(123421))


def romanToInt(s):

    numerals = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    if len(s) == 1:
        return numerals[s[0]]

    last_number = 0
    result = 0
    is_adding = True

    # step thrugh string in reverse
    for c in s[::-1]:     
        # if numeral is better always add to result   
        if numerals[c] > last_number:
            is_adding = True
            result += numerals[c]
        # handle for multiple similiar
        elif numerals[c] == last_number:
            if is_adding: 
                result += numerals[c]
            else:
                result -= numerals[c]
        # handle for subtraction
        elif numerals[c] < last_number:
            is_adding = False
            result -= numerals[c]
        last_number = numerals[c]
    return result



print('roman numeral')
print(romanToInt('IIV'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))
print(romanToInt('IV'))

# is valid
print('START STACK')
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []

    if len(s) == 1:
        return False

    if s == '':
        return True
    

    valids = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char in '({[':
            stack.append(char)   
        else:
            if len(stack) > 0 and valids[char] == stack[-1]:
                stack.pop()
            else:
                return False                      

    return True if len(stack) == 0 else False

print(isValid(']'))
print(isValid('()[]{}'))
print(isValid('([)]'))
print(isValid('{[]}'))



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists2(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """    
    new_list = ListNode(0)
    current = new_list
        
    while l1 and l2:
        # print('node value1 {} node value2 {}'.format(list_node1.val, list_node2.val))
        if l1.val <= l2.val:           
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2         
            l2 = l2.next
        current = current.next

    if l1 is None:
        current.next = l2

    if l2 is None:
        current.next = l1


    return new_list.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

print(mergeTwoLists2(list1, list2))

list1 = ListNode(2)


list2 = ListNode(1)

print(mergeTwoLists2(list1, list2))



#  REMOVING DUPLICATES

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    x = 1
    while x < len(nums):
        if nums[x] == nums[x-1]:
            del nums[x]          
        else:  
            x += 1

    return len(nums)



print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,0,0,0]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))



def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    if nums == []:
        return 0
    if len(nums) == 1:
        if nums[0] == val:              
            nums[0] = None
            return 0
        else:                
            return 1
    
    i = 0
    for j in range(0, len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i+= 1

        
    return i

nums = [3,2,2,3]
print(removeElement(nums, 3))
print(nums)


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int        
    """
    
    if nums == []:
        return 0

    for i in range(0, len(nums)):
        if target <= nums[i]:
            return i
        
    # if nothing is found return last index   
    return len(nums) 
    
def searchInsert2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int        
    """
    low = 0
    high = len(nums) - 1
    not_found = 0
    while low <= high:      
        mid = (low + high)//2        
        guess = nums[mid]
        if guess == target:
            return mid
        if target < guess:
            high = mid - 1
            not_found = mid
        else:
            low = mid + 1
            not_found = low
    return not_found   


print(searchInsert2([1,3,5,6], 5))
print(searchInsert2([1,3,5,6], 2))
print(searchInsert2([1,3,5,6], 7))
print(searchInsert2([1,3,5,6], 0))

def maxSubArraySum(nums): 
    if len(nums) == 1:
        return nums[0]

    max_total = nums[0]
    max_current = nums[0]

    for x in nums[1:]:
        # print('x at begginging ', x)
        max_current = max_current + x
        if x > max_current:
            max_current = x

        if max_current > max_total:
            max_total = max_current

        # print('loop ending max total', max_total)
    
    return max_total

print(maxSubArraySum([-2,-1]))
print(maxSubArraySum([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArraySum([-1,-2]))


def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    if len(arr) == 1:
        return arr[0]
    max_total = 0
    max_current = 0
    
    for num in arr:
        max_current = max_current + num
        if max_current < 0:
            max_current = 0
        if max_total < max_current:
            max_total = max_current
    
    
    return max_total

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = max_sum_subarray(arr)
    print(solution)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")
        
arr= [1, 2, 3, -4, 6]
solution= 8 # sum of array

test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)

arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)