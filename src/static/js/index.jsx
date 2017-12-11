import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  render() {
    return (
      <div className="default-container">
        <h1>Hello World!</h1>
        <p>This is a Django + React.js Template</p>
      </div>
    );
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('react-app')
);
