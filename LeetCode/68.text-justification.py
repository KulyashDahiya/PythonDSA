#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res  = []
        cur_line = []
        cur_len = 0

        for word in words:
            if len(word) + cur_len + len(cur_line) > maxWidth:
                
                space_to_dis = maxWidth - cur_len

                if len(cur_line) == 1:
                    res.append(cur_line[0] +  ' ' * space_to_dis)
                else:
                    equal_space = space_to_dis  // (len(cur_line) - 1)
                    extra_space = space_to_dis % (len(cur_line) - 1)

                    for i in range(len(cur_line) - 1):
                        cur_line[i] += ' ' * equal_space
                        if extra_space > 0:
                            cur_line[i] += ' '
                            extra_space -= 1
                
                    res.append(''.join(cur_line))

                cur_line = []
                cur_len = 0
            
            cur_line.append(word)
            cur_len += len(word)

        last_line = ' '.join(cur_line)
        res.append(last_line + ' ' * (maxWidth - len(last_line)) )

        return res

        
# @lc code=end

