from queue import deque

class SyntacticAnalysis:
    """
    Syntactic Analysis is a class that implements the syntactic analysis of a given input.
    """

    def __init__(self):
        self.__stack: deque = deque()
        self.__queue: deque = deque()
        self.__label = 1  # Initial label

    def __generate_label(self):
        label = self.__label
        self.__label += 1
        return label

    def __program(self, input_data: list) -> tuple:
        """
        Program is a method that implements the program syntax analysis.
        Args:
            input_data (list): List of tuples containing:
                - str: Token symbol
                - str: Token lexeme
        Returns:
            tuple: A tuple containing:
                - bool: True if the input data is accepted, False otherwise
                - list: List of errors messages
        """
        accepted: bool = True
        errors: list = []

        self.__label = 1  # Reset the label counter for each new program

        # Process the input_data according to the program syntax rules

        return (accepted, errors)

    def analyze(self, input_data: list) -> tuple:
        """
        Analyze is a method that initiates the syntactic analysis.
        Args:
            input_data (list): List of tuples containing:
                - str: Token symbol
                - str: Token lexeme
        Returns:
            tuple: A tuple containing:
                - bool: True if the input data is accepted, False otherwise
                - list: List of errors messages
        """
        return self.__program(input_data)

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Assuming each line contains a token symbol and token lexeme separated by a space
    input_data = [line.strip().split() for line in lines]
    return input_data

def write_output_to_file(file_path, output_data):
    with open(file_path, 'w') as file:
        for item in output_data:
            file.write(str(item) + '\n')

if __name__ == "__main__":
    input_file_path = 'sint2.txt'  # Path to the input file
    output_file_path = 'resSint2.txt'  # Path to the output file

    input_data = read_input_from_file(input_file_path)

    syntactic_analyzer = SyntacticAnalysis()
    result, errors = syntactic_analyzer.analyze(input_data)

    output_data = ["Accepted: " + str(result), "Errors: " + str(errors)]

    write_output_to_file(output_file_path, output_data)
