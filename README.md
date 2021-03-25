# Parser for the site rabota.by
This parser searches for vacancies by name and searches for keywords in the description of found vacancies according to the data entered by the user.
# How it works?
1. Download this repository by clicking "Code" -> "Download ZIP" or clone the repository with the
   command: `git clone https://github.com/AlexandraLos/parser.git`
2. Install the list of external dependencies with the command:
`pip install -r requirements.txt`
3. Run the file called "app.py"
4. Enter the name of the job you are looking for, for example "python"
5. Enter search keywords separated by a space, for example "python linux flask"
6. Enjoy the result :)
# Are there any tests?
Yes, the test file is called "test_pars.py" and is located in the "tests" folder. 
To run tests with detailed information, enter the command in the terminal:
`pytest -v test_pars.py`
