def display(current_URL):
    print("Your current URL is: ", current_URL)

    options = []

    if current_URL == base_url:
        options.append("Courses")
        options.append("Opportunities")
    elif current_URL == base_url + "Courses":
        options.append("CFGDegree")
        options.append("Back")
    elif current_URL == base_url + "Opportunities":
        options.append("Ambassadors")
        options.append("Back")
    elif current_URL == base_url + "Courses/CFGDegree":
        options.append("Back")
    elif current_URL == base_url + "Opportunities/Ambassadors":
        options.append("Back")

    for x, option in enumerate(options, start=1):
        print(f"{x}. {option}")

    
    choice = input("Please select an option: ")  
    return options[int(choice) - 1] if choice.isdigit() else choice


base_url = "https://codefirstgirls.com/"
current_URL = base_url


while True:
    next_page = display(current_URL)
    if next_page == "Back":
        if current_URL == base_url:
            break
        current_URL = current_URL.rsplit('/', 2)[0] + '/'
        print("\n")
    else:
        current_URL = current_URL + next_page + '/'
        print("\n")

 # Question 3.B

# Time Complexity: 

# The number of If - else statements is constant and does not depend on the input. (Note, if these were to include loops or recursion they would no longer be considered constant).
# With the for loop, the number of options is constant because they are limited.
# The input line is constant.

# The majority of the lines in this program are constant, because they do not rely on the input size. This is because the number of executions is limited or set. 
# Constants = O(1). So the time complexity of this program is O(1).

# Space Complexity: 

# The same goes for the space complexity. The variables used are constant, because the maximum number of elements added to options = [] is constant. 

# Therefore, the space complexity is also O(1) because it is not determined by the input size. 

#Marks (8/15)
# Instead of using if else conditions you can use a dictionary to store the url and options as key value pairs. This will improve the efficiency of your program.
# You can make your solution simpler by using a data structure like a 'list' to add URLs using 'append' and remove them using 'pop'.
