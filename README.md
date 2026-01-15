# CS50-Final-Project (Quiz Application)

#### Description:

The Quiz Application is a command-line based program developed as the final project for CS50. The goal of this project is to create an interactive quiz system that allows users to test their Python general knowledge in an engaging and structured way. The application emphasizes clean program design, file handling, user input validation, and modular code organization using Python.

When the program starts, the user is prompted to enter their name and select a difficulty level: easy, medium, or hard. This design choice was made to provide flexibility and allow users of different skill levels to participate. Based on the selected difficulty, the program loads questions from a corresponding CSV file. Each CSV file contains multiple questions, their possible options, and the correct answer. This separation of questions by difficulty improves clarity and scalability, making it easy to add or modify questions in the future without changing the core program logic.

The main logic of the application resides in `project.py`. This file contains the main function that controls program flow, handles user input, and coordinates the quiz process. It includes helper functions such as `level()` to map user input to the correct CSV file, `generate_quiz()` to iterate through the questions and track the score, and `ask_questions()` to display each question, shuffle the options randomly, and evaluate the user’s answer. Randomizing the options was a deliberate design decision to prevent memorization of answer positions and to make the quiz more challenging and fair.

The project uses exception handling extensively to ensure the program does not crash due to invalid user input. For example, when a user enters an invalid option number or a non-integer value, the program safely handles the error and continues execution. This improves the robustness and user experience of the application. At the end of the quiz, the user’s final score is displayed and saved to a file named `result.txt`, along with their name and chosen difficulty level. This allows results to persist across multiple runs of the program.

The question data is stored in three separate files: `easy.csv`, `medium.csv`, and `hard.csv`. Each CSV file contains columns for the question, available options, and the correct answer. Using CSV files was a conscious choice because they are simple, human-readable, and easy to process using Python’s built-in `csv` module.

To ensure correctness and reliability, automated tests are included in `test_project.py`. This file contains Pytest-based unit tests that verify key functions such as difficulty selection and file handling. Writing tests helped validate program behavior and ensured that changes did not introduce unintended bugs.

Overall, this project demonstrates practical use of Python fundamentals, including functions, loops, file I/O, exception handling, randomness, and testing. The Quiz Application is designed to be simple to use, easy to extend, and well-structured, reflecting the programming principles taught throughout CS50.
