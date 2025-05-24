# Sudoku Solver
This is my attempt at producing a sudoku solver application. 
## Project Structure
```
├── README.md
├── src
│   ├── app.py
│   ├── frame.py
│   ├── utils.py
│   ├── window.py
├── test
│   ├── test.py
├── dist
│   ├── app.exe
├── .venv
├── .vscode
│   ├── settings.json
├── .env
├── requirements.txt
└── .gitignore
```
### Running the application
**(.venv) requirements:** customtkinter==5.2.2  
**.env:** PYTHONPATH=./src  
**.vscode/settings.json:**
{
  "python.envFile": "${workspaceFolder}/.env"
}

**Run:**  
--*app.py*  
--*dist/app.exe*
 
## Application Interface
![alt text](readme/sudoku.png)  
*Main Interface*  

![alt text](readme/filled_grid.png)  
*Sudoku grid filled*  

![alt text](readme/solved_grid.png)  
*Solved sudoku grid*

![alt text](readme/invalid_grid.png)  
*Invalid sudoku grid (invalid squares are highlighted)*  

![alt text](readme/load_grid.png)  
*Loading a grid with a string*  

![alt text](readme/error_msg.png)  
*Error Message from entering invalid string*  