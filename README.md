# FormulaManager
Standalone Manager for Salt Formulas with Forms.

## Dev Setup
### Preparations
- Install [Node.js](https://nodejs.org/en/)
- Clone the git repo: `git clone git@github.com:benediktwerner/FormulaManager.git`
- Change directory: `cd FormulaManager`
- Install Node dependencies: `npm install`
- Install python dependencies: `pip3 -r requirements.txt` (Just `pip` if you only have Python 3)

### Run
- Start the flask server that serves the formula data: `./server.py`
- Start the Node server that serves the Web UI: `npm start`
- This should automatically open a browse window. If not go to `http://localhost:3000`
- The page will auto-reload on changes to JavaScript files
- The flask server serves the formula from the `test_formula.yml` file.
