#Task 01
'''Generate a Python program that implements the Merge Sort algorithm.
Requirements:Create a function named merge_sort(arr) that sorts a list in ascending order. Include a proper docstring explaining the algorithm.Mention time complexity and space complexity in the docstring.
Add sample test cases to verify the correctness of the function.The program should be simple and easy to understand.'''
'''def merge_sort(arr):
    """
    Sorts a list in ascending order using the Merge Sort algorithm.

    The Merge Sort algorithm is a divide-and-conquer sorting algorithm that works by recursively dividing the list into smaller sublists until each sublist contains a single element. Then, it merges those sublists back together in a sorted order.

    Time Complexity: O(n log n) - This is because the list is divided into two halves log n times, and each merge operation takes O(n) time.
    Space Complexity: O(n) - This is because we need additional space to hold the temporary arrays during the merge process.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: A new list containing the sorted elements.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)
def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Parameters:
    left (list): The first sorted list.
    right (list): The second sorted list.

    Returns:
    list: A new list containing the merged and sorted elements from both input lists.
    """
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are remaining elements in the left or right list, add them to the merged list
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged
# Sample test cases
if __name__ == "__main__":
    test_cases = [
        [38, 27, 43, 3, 9, 82, 10],
        [5, 2, 9, 1, 5, 6],
        [12, 11, 13, 5, 6, 7],
        [],
        [1],
        [2, 1]
    ]

    for i, test in enumerate(test_cases):
        sorted_list = merge_sort(test)
        print(f"Test Case {i + 1}: {sorted_list}")'''
#Task 02
'''Create a Python function binary_search(arr, target) to find a target element in a sorted list.
The function should return the index if the element is found, otherwise return -1. Include a docstring explaining best, average, and worst-case time complexities. Also add some test cases.'''
'''def binary_search(arr, target):
    """
    Performs binary search to find the target element in a sorted list.

    Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

    Time Complexities:
    - Best Case: O(1) - This occurs when the target element is at the middle of the list.
    - Average Case: O(log n) - This occurs when the target element is randomly located in the list.
    - Worst Case: O(log n) - This occurs when the target element is not present in the list or is located at one of the ends.

    Parameters:
    arr (list): A sorted list of elements.
    target: The element to be searched for.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            left = mid + 1
        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Target was not found in the list
    return -1
# Sample test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 3),  # Target is in the middle
        ([1, 2, 3, 4, 5], 1),  # Target is at the beginning
        ([1, 2, 3, 4, 5], 5),  # Target is at the end
        ([1, 2, 3, 4, 5], 6),  # Target is not present
        ([], 1),               # Empty list
        ([1], 1),              # Single element list where target is present
        ([1], 0)               # Single element list where target is not present
    ]

    for i, (arr, target) in enumerate(test_cases):
        result = binary_search(arr, target)
        print(f"Test Case {i + 1}: Target {target} in {arr} -> Index: {result}")'''
#Task 03
'''Create a simple Python program for a healthcare appointment system that searches appointments using appointment ID and sorts appointments by time and consultation fee.
Recommend suitable searching and sorting algorithms with justification and implement them with test cases.'''
'''class Appointment:
    def __init__(self, appointment_id, time, consultation_fee):
        self.appointment_id = appointment_id
        self.time = time
        self.consultation_fee = consultation_fee

    def __repr__(self):
        return f"Appointment(ID: {self.appointment_id}, Time: {self.time}, Fee: {self.consultation_fee})"
class HealthcareAppointmentSystem:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def search_appointment_by_id(self, appointment_id):
        """
        Searches for an appointment by its ID using linear search.

        Justification: Since the appointments are not guaranteed to be sorted by ID, linear search is a suitable choice for searching through the list of appointments.

        Time Complexity: O(n) - In the worst case, we may have to check every appointment in the list.
        """
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                return appointment
        return None

    def sort_appointments_by_time(self):
        """
        Sorts appointments by time using Merge Sort.

        Justification: Merge Sort is an efficient sorting algorithm with a time complexity of O(n log n) and is stable, which means it maintains the relative order of records with equal keys (in this case, consultation fees).

        Time Complexity: O(n log n)
        """
        self.appointments = merge_sort(self.appointments, key=lambda x: x.time)

    def sort_appointments_by_fee(self):
        """
        Sorts appointments by consultation fee using Merge Sort.

        Justification: Similar to sorting by time, Merge Sort is efficient and stable for sorting by consultation fee.

        Time Complexity: O(n log n)
        """
        self.appointments = merge_sort(self.appointments, key=lambda x: x.consultation_fee)
def merge_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], key)
    right_half = merge_sort(arr[mid:], key)

    return merge(left_half, right_half, key)
def merge(left, right, key):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if key(left[left_index]) < key(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged
# Sample test cases
if __name__ == "__main__":
    system = HealthcareAppointmentSystem()
    system.add_appointment(Appointment(1, "10:00 AM", 100))
    system.add_appointment(Appointment(2, "11:00 AM", 150))
    system.add_appointment(Appointment(3, "09:00 AM", 80))

    print("Appointments before sorting:")
    print(system.appointments)

    system.sort_appointments_by_time()
    print("\nAppointments sorted by time:")
    print(system.appointments)

    system.sort_appointments_by_fee()
    print("\nAppointments sorted by consultation fee:")
    print(system.appointments)

    search_result = system.search_appointment_by_id(2)
    print("\nSearch for appointment with ID 2:")
    print(search_result)
    search_result = system.search_appointment_by_id(4)
    print("\nSearch for appointment with ID 4 (not found):")
    print(search_result)'''
    #Task 04
'''Suggest an efficient searching and sorting algorithm for a Railway Ticket Reservation System that stores ticket ID, passenger name, train number, seat number, and travel date. 
The system needs to search tickets using ticket ID and sort bookings based on travel date or seat number. 
Justify the choice of algorithms and provide simple Python implementation.'''
'''class Ticket:
    def __init__(self, ticket_id, passenger_name, train_number, seat_number, travel_date):
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.train_number = train_number
        self.seat_number = seat_number
        self.travel_date = travel_date

    def __repr__(self):
        return f"Ticket(ID: {self.ticket_id}, Name: {self.passenger_name}, Train: {self.train_number}, Seat: {self.seat_number}, Date: {self.travel_date})"
class RailwayTicketReservationSystem:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def search_ticket_by_id(self, ticket_id):
        """
        Searches for a ticket by its ID using linear search.

        Justification: Since the tickets are not guaranteed to be sorted by ID, linear search is a suitable choice for searching through the list of tickets.

        Time Complexity: O(n) - In the worst case, we may have to check every ticket in the list.
        """
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None

    def sort_tickets_by_date(self):
        """
        Sorts tickets by travel date using Merge Sort.

        Justification: Merge Sort is an efficient sorting algorithm with a time complexity of O(n log n) and is stable, which means it maintains the relative order of records with equal keys (in this case, seat numbers).

        Time Complexity: O(n log n)
        """
        self.tickets = merge_sort(self.tickets, key=lambda x: x.travel_date)

    def sort_tickets_by_seat_number(self):
        """
        Sorts tickets by seat number using Merge Sort.

        Justification: Similar to sorting by travel date, Merge Sort is efficient and stable for sorting by seat number.

        Time Complexity: O(n log n)
        """
        self.tickets = merge_sort(self.tickets, key=lambda x: x.seat_number)
# Sample test cases
if __name__ == "__main__":
    system = RailwayTicketReservationSystem()
    system.add_ticket(Ticket(1, "Alice", "Train A", "1A", "2024-07-01"))
    system.add_ticket(Ticket(2, "Bob", "Train B", "2B", "2024-06-30"))
    system.add_ticket(Ticket(3, "Charlie", "Train A", "1B", "2024-07-02"))

    print("Tickets before sorting:")
    print(system.tickets)

    system.sort_tickets_by_date()
    print("\nTickets sorted by travel date:")
    print(system.tickets)

    system.sort_tickets_by_seat_number()
    print("\nTickets sorted by seat number:")
    print(system.tickets)

    search_result = system.search_ticket_by_id(2)
    print("\nSearch for ticket with ID 2:")
    print(search_result)
    search_result = system.search_ticket_by_id(4)
    print("\nSearch for ticket with ID 4 (not found):")
    print(search_result)'''
# Task 05
'''Recommend suitable searching and sorting algorithms for a Railway Ticket Reservation System that stores ticket ID, passenger name, train number, seat number, and travel date. 
The system should search tickets using ticket ID and sort bookings based on travel date or seat number.
Explain why the algorithms are efficient and provide a simple Python implementation.'''
# The recommended searching algorithm for searching tickets by ticket ID is linear search, as the tickets are not guaranteed to be sorted by ID. Linear search is simple and effective for small datasets, with a time complexity of O(n).
# For sorting bookings based on travel date or seat number, Merge Sort is recommended. Merge Sort is an efficient sorting algorithm with a time complexity of O(n log n) and is stable, meaning it maintains the relative order of records with equal keys (in this case, seat numbers or travel dates). This makes it suitable for sorting complex data structures like tickets.
# The implementation of the Railway Ticket Reservation System with the recommended algorithms is provided in Task 04 above.
def merge_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid], key)
    right_half = merge_sort(arr[mid:], key)

    return merge(left_half, right_half, key)
def merge(left, right, key):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if key(left[left_index]) < key(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged






















