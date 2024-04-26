# Define data
num_trucks = 5
num_vans = 3
num_routes = 10

distance_matrix = [[0 for _ in range(num_routes)] for _ in range(num_routes)]
for i in range(num_routes):
  for j in range(i, num_routes):
    distance_matrix[i][j] = distance_matrix[j][i] = i + j + 1  # Sample increasing distances

route_data = []
for i in range(num_routes):
  route_data.append({
      "distance": distance_matrix[i][i],
      "vehicle_capacity": 1 + i % 2,
      "vehicle_type": None
  })

assignments = [-1 for _ in range(num_routes)]


def nearest_neighbor(route_idx):
  """
  Finds the closest unassigned route to the given route
  """
  best_route_idx = -1
  best_distance = float('inf')
  for i in range(num_routes):
    if assignments[i] == -1 and distance_matrix[route_idx][i] < best_distance:
      best_route_idx = i
      best_distance = distance_matrix[route_idx][i]
  return best_route_idx


total_distance = 0
for van_idx in range(num_vans):
  # Start with any unassigned route
  current_route_idx = next(i for i, v in enumerate(assignments) if v == -1)
  for _ in range(route_data[current_route_idx]["vehicle_capacity"]):
    # Find nearest unassigned route and assign the van
    next_route_idx = nearest_neighbor(current_route_idx)
    assignments[next_route_idx] = van_idx
    total_distance += distance_matrix[current_route_idx][next_route_idx]
    current_route_idx = next_route_idx

remaining_trucks = num_trucks
for route_idx in range(num_routes):
  if assignments[route_idx] == -1 and remaining_trucks > 0:
    assignments[route_idx] = num_vans + remaining_trucks - 1
    remaining_trucks -= 1
    total_distance += distance_matrix[current_route_idx][route_idx]

# Print the assignments
print("Route Assignments:")
for route_idx in range(num_routes):
  vehicle_type = "Truck" if assignments[route_idx] >= num_vans else "Van"
  print(f"Route {route_idx+1}: Assigned to {vehicle_type} {assignments[route_idx] + 1}")

# Print total distance traveled
print(f"\nTotal Distance Traveled: {total_distance}")
