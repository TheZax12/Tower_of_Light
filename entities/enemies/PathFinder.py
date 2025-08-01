import heapq

from gameMap.MapPosition import MapPosition
from gameMap.MapSettings import map_width, map_height


class PathNode:
    def __init__(self, position: MapPosition, g=0, h=0, parent=None):
        self.position = position
        self.g = g
        self.h = h
        self.parent = parent

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

    def __eq__(self, other):
        return self.position == other.position

    def __hash__(self):
        return hash(self.position)


class PathFinder:
    def __init__(self, game_map):
        self.game_map = game_map

    def heuristic(self, a: MapPosition, b: MapPosition):
        return a.distance_to(b)

    def find_path(self, start_position: MapPosition, goal_position: MapPosition, max_steps=50):
        start_node = PathNode(start_position, 0, self.heuristic(start_position, goal_position))
        open_heap = [start_node]
        open_set = {start_position}
        closed_set = set()
        g_costs = {start_position: 0}

        steps = 0
        while open_heap and steps < max_steps:
            steps += 1
            current_node = heapq.heappop(open_heap)
            open_set.discard(current_node.position)

            if current_node.position == goal_position:
                path = []
                temp = current_node
                while temp:
                    path.append(temp.position)
                    temp = temp.parent
                return path[::-1]

            closed_set.add(current_node.position)

            neighbors = [
                current_node.position.above(),
                current_node.position.below(),
                current_node.position.left(),
                current_node.position.right()
            ]

            for neighbor_position in neighbors:
                nx, ny = neighbor_position.get_x(), neighbor_position.get_y()

                if not (0 <= nx < map_width and 0 <= ny < map_height):
                    continue

                tile = self.game_map.map_tiles[ny][nx]
                if not tile.is_walkable():
                    continue

                if neighbor_position in closed_set:
                    continue

                tentative_g = current_node.g + 1

                if tentative_g < g_costs.get(neighbor_position, float('inf')):
                    g_costs[neighbor_position] = tentative_g
                    h_cost = self.heuristic(neighbor_position, goal_position)
                    neighbor_node = PathNode(neighbor_position, tentative_g, h_cost, current_node)
                    if neighbor_position not in open_set:
                        heapq.heappush(open_heap, neighbor_node)
                        open_set.add(neighbor_position)
        return []