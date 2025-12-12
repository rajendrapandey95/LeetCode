class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda e: (int(e[1]), e[0] == "MESSAGE"))

        count = [0] * numberOfUsers
        next_online_time = [0] * numberOfUsers

        for event in events:
            cur_time = int(event[1])

            if event[0] == "MESSAGE":
                target = event[2]

                if target == "ALL":
                    for i in range(numberOfUsers):
                        count[i] += 1

                elif target == "HERE":
                    for i in range(numberOfUsers):
                        if next_online_time[i] <= cur_time:
                            count[i] += 1

                else:
                    mentions = target.split(",")     
                    for m in mentions:
                        uid = int(m[1:])           
                        if 0 <= uid < numberOfUsers:
                            count[uid] += 1

            else:
                user = int(event[2])
                next_online_time[user] = cur_time + 60

        return count
