class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(n):
            #print(n)
            if len(n) ==1:
                return TreeNode(n[0])
            elif len(n) == 0:
                return None
            else:
                mid = (len(n)//2)
                print(mid)
                root = TreeNode(n[mid])


            root.left=dfs(n[:mid])
            root.right=dfs(n[mid+1:])
            return root

        return dfs(nums)