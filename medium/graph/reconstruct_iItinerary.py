from collections import deque


class Solution():
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        def build_graph(tickets):
            graph = {}
            for from_airport, to_airport in tickets:
                if from_airport in graph:
                    graph[from_airport].append(to_airport)
                else:
                    graph[from_airport] = [to_airport]
            return graph

        def build_itinerary_from(init_ticket, possible_combo_tickets, graph):
            seen_tickets = set()
            queue = deque()
            queue.append([init_ticket])

            paths = []
            while queue:
                curent_path = queue.popleft()

                print(curent_path)

                # if len(curent_path) == len(possible_combo_tickets):
                #     paths.append(curent_path)
                #     continue

                last_ticket = curent_path[len(curent_path) - 1]

                [from_air, to_air] = last_ticket

                joined_ticket = "".join([from_air, to_air])
                if joined_ticket not in seen_tickets:
                    seen_tickets.add(joined_ticket)
                    for next_dest in graph[to_air]:
                        if "".join([to_air, next_dest]) not in seen_tickets:
                            queue.append(curent_path + [[to_air, next_dest]])

        graph = build_graph(tickets)
        print(graph)

        for start in graph['JFK']:
            possible_combo_tickets = ["".join(ticket) for ticket in tickets]
            itineraries = build_itinerary_from(
                ['JFK', start], possible_combo_tickets, graph)


# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]


tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
# tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
#     "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
sol = Solution()
sol.findItinerary(tickets)
