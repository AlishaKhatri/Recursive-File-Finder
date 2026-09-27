"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os


# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    """
    Recursively calculate the sum of a list of numbers.
    """

    # Base case: an empty list has a sum of 0
    if len(numbers) == 0:
        return 0

    # Recursive case
    return numbers[0] + sum_list(numbers[1:])


def count_even(numbers):
    """
    Recursively count how many even numbers are in a list.
    """

    # Base case: an empty list contains no even numbers
    if len(numbers) == 0:
        return 0

    # If the first number is even, count it
    if numbers[0] % 2 == 0:
        return 1 + count_even(numbers[1:])

    # Otherwise move to the rest of the list
    return count_even(numbers[1:])


def find_strings_with(strings, target):
    """
    Recursively find all strings that contain a target substring.
    """

    # Base case: empty list
    if len(strings) == 0:
        return []

    # Search the remaining strings
    matches = find_strings_with(strings[1:], target)

    # If the first string contains the target, add it
    if target in strings[0]:
        return [strings[0]] + matches

    return matches


# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================

def count_files(directory_path):
    """
    Recursively count all files in a directory and its subdirectories.

    Args:
        directory_path (str): Path to the directory to analyze

    Returns:
        int: Total number of files in the directory tree
    """

    # Base case: if the path is a file, count it
    if os.path.isfile(directory_path):
        return 1

    total_files = 0

    # Look through everything inside the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        # Recursively count files
        total_files += count_files(item_path)

    return total_files


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path, extension=".encrypted"):
    """
    Recursively find all files with a specific extension.

    Args:
        directory_path (str): Path to the directory to analyze
        extension (str): File extension to search for

    Returns:
        list: List of paths to infected files
    """

    # Base case: if this is a file, check the extension
    if os.path.isfile(directory_path):

        if directory_path.endswith(extension):
            return [directory_path]

        return []

    infected_files = []

    # Search everything inside the directory
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        infected_files.extend(
            find_infected_files(item_path, extension)
        )

    return infected_files


# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":

    print("RECURSION ASSIGNMENT")
    print("=" * 50)


    # ------------------------------------------------------------------------
    # PART 1 TESTS
    # ------------------------------------------------------------------------

    print("\nPART 1: RECURSION WARM-UP TESTS")

    print(
        "sum_list([1, 2, 3, 4]) =",
        sum_list([1, 2, 3, 4]),
        "(expected: 10)"
    )

    print(
        "sum_list([]) =",
        sum_list([]),
        "(expected: 0)"
    )

    print(
        "sum_list([5, 5, 5]) =",
        sum_list([5, 5, 5]),
        "(expected: 15)"
    )

    print()

    print(
        "count_even([1, 2, 3, 4, 5, 6]) =",
        count_even([1, 2, 3, 4, 5, 6]),
        "(expected: 3)"
    )

    print(
        "count_even([1, 3, 5]) =",
        count_even([1, 3, 5]),
        "(expected: 0)"
    )

    print(
        "count_even([2, 4, 6]) =",
        count_even([2, 4, 6]),
        "(expected: 3)"
    )

    print()

    result1 = find_strings_with(
        ["hello", "world", "help", "test"],
        "hel"
    )

    print(
        "find_strings_with test 1 =",
        result1,
        "(expected: ['hello', 'help'])"
    )

    result2 = find_strings_with(
        ["cat", "dog", "bird"],
        "z"
    )

    print(
        "find_strings_with test 2 =",
        result2,
        "(expected: [])"
    )


    # ------------------------------------------------------------------------
    # PART 2: COUNT FILES TESTS
    # ------------------------------------------------------------------------

    print("\n" + "=" * 50)
    print("PART 2: COUNT FILES TESTS")

    print(
        "Total files (Test Case 1):",
        count_files("test_cases/case1_flat"),
        "(expected: 5)"
    )

    print(
        "Total files (Test Case 2):",
        count_files("test_cases/case2_nested"),
        "(expected: 4)"
    )

    print(
        "Total files (Test Case 3):",
        count_files("test_cases/case3_infected"),
        "(expected: 5)"
    )


    # ------------------------------------------------------------------------
    # COUNT FILES IN BREACH DATA
    # ------------------------------------------------------------------------

    print("\n" + "=" * 50)
    print("BREACH FILE COUNT")

    total_files = count_files("breach_data")

    print(
        "Total files in breach_data:",
        total_files
    )


    # ------------------------------------------------------------------------
    # PART 3: INFECTED FILE TESTS
    # ------------------------------------------------------------------------

    print("\n" + "=" * 50)
    print("PART 3: INFECTED FILE TESTS")

    print(
        "Total Infected Files (Test Case 1):",
        len(
            find_infected_files(
                "test_cases/case1_flat"
            )
        ),
        "(expected: 0)"
    )

    print(
        "Total Infected Files (Test Case 2):",
        len(
            find_infected_files(
                "test_cases/case2_nested"
            )
        ),
        "(expected: 0)"
    )

    print(
        "Total Infected Files (Test Case 3):",
        len(
            find_infected_files(
                "test_cases/case3_infected"
            )
        ),
        "(expected: 3)"
    )


    # ------------------------------------------------------------------------
    # FIND INFECTED FILES IN BREACH DATA
    # ------------------------------------------------------------------------

    print("\n" + "=" * 50)
    print("BREACH INFECTION ANALYSIS")

    infected_files = find_infected_files(
        "breach_data"
    )

    print(
        "Total infected files in breach_data:",
        len(infected_files)
    )


    # ------------------------------------------------------------------------
    # OPTIONAL: PRINT ALL INFECTED FILE PATHS
    # ------------------------------------------------------------------------

    # Uncomment the lines below if you want to display
    # every infected file path in the terminal.

    # print("\nINFECTED FILE LOCATIONS:")
    # for file_path in infected_files:
    #     print(file_path)


    # ------------------------------------------------------------------------
    # PART 5: DEPARTMENT ANALYSIS
    # ------------------------------------------------------------------------

    print("\n" + "=" * 50)
    print("INFECTED FILES BY DEPARTMENT")

    departments = [
        "Finance",
        "HR",
        "Sales"
    ]

    department_counts = {}

    for department in departments:

        infected_count = 0

        # Check folders directly inside breach_data
        for folder in os.listdir("breach_data"):

            folder_path = os.path.join(
                "breach_data",
                folder
            )

            # Handles folder names such as:
            # Finance
            # Finance_1
            # HR
            # HR_1
            # Sales
            # Sales_1
            if (
                os.path.isdir(folder_path)
                and (
                    folder == department
                    or folder.startswith(
                        department + "_"
                    )
                )
            ):

                department_files = find_infected_files(
                    folder_path
                )

                infected_count += len(
                    department_files
                )

        department_counts[department] = infected_count

        print(
            department + ":",
            infected_count
        )


    # ------------------------------------------------------------------------
    # DETERMINE WHICH DEPARTMENT WAS HIT HARDEST
    # ------------------------------------------------------------------------

    hardest_hit = max(
        department_counts,
        key=department_counts.get
    )

    print(
        "\nDepartment with the most infected files:",
        hardest_hit
    )

    print(
        "Number of infected files:",
        department_counts[hardest_hit]
    )


    print("\n" + "=" * 50)
    print("ANALYSIS COMPLETE")