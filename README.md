# Drone Flight Calculator

## Description

This project calculates estimated drone flight time based on payload weight. It also generates a table of flight times for different payload weights.

## Functions

- `calculate_flight_time(weight_grams)` calculates the estimated active flight time based on payload weight.
- `flight_time_table(max_weight_grams, step_grams)` creates a table of weights and their corresponding flight times.

## Testing

The project uses pytest to test the flight-time calculation, including zero payload, a typical payload, a heavy payload that reaches zero flight time, and negative payload validation.

All tests pass successfully.

## AI Use

I used GitHub Copilot's inline suggestions while developing `flight_calculator.py`. I accepted a correct suggestion, edited a suggestion to better fit the program, and rejected a suggestion that was not appropriate. I also reviewed the generated code and verified that the program and pytest tests work correctly.

## Author

Satya Moorjani