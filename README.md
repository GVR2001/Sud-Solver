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

**run:** *app.py*
## Application Interface
![alt text](sudoku.png)  
*Main Interface*  

![alt text](filled_grid.png)  
*Sudoku grid filled*  

![alt text](solved_grid.png)  
*Solved sudoku grid*

![alt text](invalid_grid.png)  
*Invalid sudoku grid (invalid squares are highlighted)*  

![alt text](load_grid.png)  
*Loading a grid with a string*  

![alt text](error_msg.png)  
*Error Message from entering invalid string*  