import math
def classical_eoq(setup_cost, demand_rate, holding_cost, lead_time):
  optimum_order_quantity = (2 * setup_cost * demand_rate / holding_cost) ** 0.5
  cycle_length = optimum_order_quantity / demand_rate
  effective_lead_time = lead_time - cycle_length*(math.floor(lead_time/cycle_length))
  reorder_point = effective_lead_time * demand_rate
  TC = (setup_cost + holding_cost * optimum_order_quantity / 2 * cycle_length) / cycle_length
  return optimum_order_quantity, reorder_point, TC

demand_rate = 100
setup_cost = 100
holding_cost = 0.02
lead_time = 12
optimum_order_quantity, reorder_point, TC = classical_eoq(setup_cost, demand_rate, holding_cost, lead_time)
print(f'Order {optimum_order_quantity} units whenever inventory level drops to {reorder_point} units')
print(f'Total daily inventory cost is {TC}')


