class Solution:
    def decodeString(self, decode_me: str) -> str:
        def decode(left, right) -> str:
            x = 0
            l = 0
            bal = 0
            s = ''
            ret = ''

            for i in range(left, right+1):
                c = decode_me[i]
                if c == '[':
                    if bal == 0:
                        l = i
                    
                    bal += 1
                    continue

                if c == ']':
                    if bal == 1:
                        ret += x * decode(l+1, i-1)
                        l = -1
                        x = 0
                    
                    bal -= 1
                    continue
                
                if c.isdigit():
                    ret += s
                    
                    if x == 0:
                        s = ''
                    
                    if bal == 0:
                        x *= 10
                        x += ord(c) - ord('0')
                else:
                    if bal == 0:
                        s += c
                    
                
            return ret + s
        
        return decode(0, len(decode_me)-1)

print(Solution().decodeString(decode_me="3[a]2[bc]"))
print(Solution().decodeString(decode_me="3[a2[c]]"))
print(Solution().decodeString(decode_me="2[abc]3[cd]ef"))