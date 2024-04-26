from pulp import *

# Define routes and their distances
routes = {
    'Route 1': {'distance': 50, 'vehicles_required': 2},
    'Route 2': {'distance': 30, 'vehicles_required': 1},
    'Route 3': {'distance': 40, 'vehicles_required': 2},
    'Route 4': {'distance': 60, 'vehicles_required': 1},
    'Route 5': {'distance': 20, 'vehicles_required': 1},
    'Route 6': {'distance': 70, 'vehicles_required': 2},
    'Route 7': {'distance': 55, 'vehicles_required': 2},
    'Route 8': {'distance': 45, 'vehicles_required': 1},
    'Route 9': {'distance': 25, 'vehicles_required': 1},
    'Route 10': {'distance': 35, 'vehicles_required': 2}
}

# Define available vehicles
fleet = {
    'trucks': {'quantity': 5, 'capacity': 2, 'distance_per_gallon': 10},
    'vans': {'quantity': 3, 'capacity': 1, 'distance_per_gallon': 15}
}

# Create a linear programming problem
prob = LpProblem("VehicleAllocation", LpMinimize)

# Define decision variables
route_vars = LpVariable.dicts("Route", routes.keys(), lowBound=0, cat='Integer')
vehicle_vars = LpVariable.dicts("Vehicle", fleet.keys(), lowBound=0, cat='Integer')

# Define objective function: minimize total distance traveled
prob += lpSum([routes[route]['distance'] * route_vars[route] for route in routes])

# Add constraints: each route must be covered, fleet size constraints
for route, data in routes.items():
    prob += route_vars[route] >= data['vehicles_required']

for vehicle, data in fleet.items():
    prob += lpSum([route_vars[route] for route in routes]) <= data['quantity'] * vehicle_vars[vehicle]
    prob += lpSum([route_vars[route] for route in routes]) >= data['capacity'] * vehicle_vars[vehicle]

# Solve the problem
prob.solve()

# Output results
print("Optimal vehicle allocation:")
for route, var in route_vars.items():
    print(f"{route}: {var.value()} vehicles")

print("\nTotal distance traveled:", value(prob.objective))