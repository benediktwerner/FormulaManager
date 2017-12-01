import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import './components/FormulaForm.css';

import {FormulaForm} from './components/FormulaForm.js';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Formula Manger</h1>
        </header>

        <div className="container">
          <FormulaForm
            dataUrl="http://localhost:5000/testData"
            saveUrl="http://localhost:5000/save"
            formulaId={0}
            systemId={1}
            getFormulaUrl={(id) => "/" + id}
            currentScope="system"
          />
        </div>
      </div>
    );
  }
}

export default App;
