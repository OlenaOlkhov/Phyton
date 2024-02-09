import random

# Create a list of 100 random numbers from 0 to 1000
random_numbers = [random.randint(0, 1000) for _ in range(100)]


# Function to sort the list without using sort()
def custom_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    # Call the custom sort function


custom_sort(random_numbers)


# Function to calculate average for even and odd numbers
def calculate_average(numbers):
    even_sum = 0
    odd_sum = 0
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
            even_count += 1
        else:
            odd_sum += num
            odd_count += 1
    even_average = even_sum / even_count if even_count != 0 else 0
    odd_average = odd_sum / odd_count if odd_count != 0 else 0
    return even_average, odd_average


# Call the calculate_average function
even_avg, odd_avg = calculate_average(random_numbers)

# Print both average results in the console
print("Average for even numbers:", even_avg)
print("Average for odd numbers:", odd_avg)
