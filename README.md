# tkinter-quiz

a Python Multiple Choice Quiz Application with possible multiple correct answers and a simple GUI

The Application is a simple multiple choice quiz program built with Python and Tkinter. The application loads questions and answer options from a YAML file, allows users to select their answers, and provides immediate feedback on their choices. It also supports an option to exit the quiz at any time.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Sample YAML File](#sample-yaml-file)
- [License](#license)

## Description

The Python Quiz Application allows users to take a quiz based on a set of questions and answers loaded from a YAML file. The application presents each question with shuffled answer options and allows the user to select multiple answers. Once the user clicks the "Select" button, the application evaluates the selected options and displays immediate feedback on whether each selected answer is correct or not. Additionally, the user can exit the quiz at any time during the evaluation process.

The application uses the Tkinter library for its graphical user interface and randomizes the order of questions to enhance user experience and avoid patterns.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Usage

1. Clone the repository to your local machine

2. Navigate to the project directory

3. Install the required packages (if any)

4. Prepare your own YAML file with quiz questions and answers in the format described below (see [Sample YAML File](#sample-yaml-file)).

5. Run the quiz application:

   ```bash
   python main.py
   
   options:
     -h, --help            show this help message and exit
     -i INPUTFILE, --input INPUTFILE
                           specify a .yaml-file to quiz from, defaults to `questions.yaml` if not specified
  ```

6. Answer each question by selecting the checkboxes next to the answer options. Once you've made your selections, click the "Select" button to see the evaluation results. Questions will appear in random order. Also Answers will appear in random order.

7. After the evaluation is displayed, click "OK" to proceed to the next question or exit the application.

## File Structure

The structure of the project directory is as follows:

``` filesystem
tkinter-quiz/
  ├── main.py
  ├── questions.yaml
  └── README.md
```

- `main.py`: The main Python script that runs the quiz application.
- `questions.yaml`: A sample YAML file that stores quiz questions and answers.
- `README.md`: This README file providing information about the project.

## Sample YAML File

The YAML file contains questions and their respective answers in the following format:

```yaml
- text: "What is the capital of France?"
  answers:
    - istrue: "Paris"
    - isfalse: "London"
    - isfalse: "Berlin"
    - isfalse: "Rome"

- text: "Which planet is closest to the Sun?"
  answers:
    - istrue: "Mercury"
    - isfalse: "Venus"
    - isfalse: "Mars"
    - isfalse: "Earth"

# Add more questions here...
```

- Each question is represented as a dictionary with the key `"text"` for the question text and `"answers"` for the list of answer options.
- Answer options are represented as dictionaries with either `"istrue"` or `"isfalse"` key to indicate whether the answer is correct or incorrect, respectively.

Feel free to create your own YAML file with custom questions and answers for the quiz.

## License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
