def calculate_flight_time(weight_grams):
    """Calculates the active flight time based on payload weight.
    :param weight_grams: Payload weight in grams
    :return: Estimated active flight time in minutes"""
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.")
    
    flight_time = 180 - (0.1 * weight_grams)
    if flight_time < 0:
        flight_time = 0  # Ensure flight time is not negative
    return flight_time
def flight_time_table(max_weight_grams, step_grams):
    """Generates a table of flight times for weights from 0 to max_weight_grams in increments of step_grams.
    :param max_weight_grams: Maximum payload weight in grams
    :param step_grams: Increment size for the weight values
    :return: List of tuples containing (weight, flight_time)"""
    if max_weight_grams < 0 or step_grams < 0:
        raise ValueError("Max weight and step must be positive numbers.")
    
    table = []
    for weight in range(0, max_weight_grams + 1, step_grams):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))
    return table

#Test the flight time calculation


