class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        keys = [0]*len(rooms)
        keys[0]=1
        
        def enter_room(room):
            if len(room)>0:
                for i in room:
                    if keys[i]<1:
                        keys[i]+=1
                        enter_room(rooms[i])
    
        enter_room(rooms[0])
        if 0 in keys:
            return False
        else:
            return True