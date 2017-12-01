import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

const FormulaForm = require("./components/FormulaForm").FormulaForm;

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Formula Manger</h1>
        </header>

        <FormulaForm
            dataUrl="http://localhost:5000/testData"
            addFormulaNavBar={function(){}}
            formulaId={0}
            getFormulaUrl={(id) => "/" + id}
            saveFormula={(component, values) => console.log("Save!")}
            currentScope="system"
        />
      </div>
    );
  }
}

export default App;
