class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserved_map = defaultdict(set)
        for row, seat in reservedSeats:
            reserved_map[row].add(seat)
        
        total = 0
        for row in reserved_map:
            blocked = reserved_map[row]
            left = all(seat not in blocked for seat in [2, 3, 4, 5])
            right = all(seat not in blocked for seat in [6, 7, 8, 9])
            middle = all(seat not in blocked for seat in [4, 5, 6, 7])
            
            if left and right:
                total += 2
            elif left or right or middle:
                total += 1
        
        total += 2 * (n - len(reserved_map)) 
        return total
    