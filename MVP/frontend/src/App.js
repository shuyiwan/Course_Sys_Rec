import './App.css';
import './index.css';
import Navbar from './Components/Navbar'
import About from './Pages/About'
import Courses from './Pages/Courses'
import Home from './Pages/Home'
import {Route, Routes} from 'react-router-dom'


function App() {


  return (
    
    <div className="App">
      <>
        <Navbar/>
        <div>
          <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/courses" element={<Courses/>}/>
            <Route path="/about" element={<About/>}/>
          </Routes>
        </div>
      </>
      
      <button className = "loginButton">Login</button>

      <div className="helloWorld">
        MVP
      </div>
      

    </div>

    
  );
}

export default App;
