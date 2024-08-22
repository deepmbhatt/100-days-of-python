class FlightData:
    # Initialize the FlightData class with the necessary attributes
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price  # Price of the flight
        self.origin_airport = origin_airport  # Origin airport code
        self.destination_airport = destination_airport  # Destination airport code
        self.out_date = out_date  # Departure date
        self.return_date = return_date  # Return date
        self.stops = stops  # Number of stops

def find_cheapest_flight(data):
    # Handle empty data if no flight or Amadeus rate limit exceeded
    # UPDATED to include stops!
    if data is None or not data['data']:  # Check if data is None or empty
        print("No flight data")  # Print message if no flight data
        return FlightData(
            price="N/A",  # No price available
            origin_airport="N/A",  # No origin airport available
            destination_airport="N/A",  # No destination airport available
            out_date="N/A",  # No departure date available
            return_date="N/A",  # No return date available
            stops="N/A"  # No stops information available
        )

    # Data from the first flight in the JSON response
    first_flight = data['data'][0]  # Get the first flight data
    lowest_price = float(first_flight["price"]["grandTotal"])  # Get the price of the first flight
    # A flight with 2 segments will have 1 stop
    nr_stops = len(first_flight["itineraries"][0]["segments"]) - 1  # Calculate the number of stops
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]  # Get the origin airport code
    # Final destination is found in the last segment of the flight
    destination = first_flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]  # Get the destination airport code
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]  # Get the departure date
    # Return date is the first segment of the second itinerary
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]  # Get the return date

    # Initialize FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)  # Create a FlightData object for the first flight

    # Iterate through all flights in the data to find the cheapest one
    for flight in data["data"]:  # Loop through each flight in the data
        price = float(flight["price"]["grandTotal"])  # Get the price of the current flight
        if price < lowest_price:  # Check if the current flight is cheaper
            lowest_price = price  # Update the lowest price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]  # Update the origin airport code
            destination = flight["itineraries"][0]["segments"][nr_stops]["arrival"]["iataCode"]  # Update the destination airport code
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]  # Update the departure date
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]  # Update the return date
            # Add number of stops
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)  # Update the cheapest flight data
            print(f"Lowest price to {destination} is £{lowest_price}")  # Print the lowest price and destination

    return cheapest_flight  # Return the cheapest flight data