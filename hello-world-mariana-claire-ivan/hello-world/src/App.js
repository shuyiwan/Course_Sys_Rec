import './App.css';

function LogIn() {
  return (
    <button>
      Log In
    </button>
  );
}



function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          Hello World!
        </h1>
        <h>
          This app was made with React.
        </h>
        <LogIn />
      </header>
    </div>
  );
}

export default App;
