import './Styles/App.css';
import './Styles/index.css';
import Navbar from './Components/Navbar'
import About from './Pages/About'
import Search from './Pages/Search'
import CourseCart from './Pages/CourseCart';
import Home from './Pages/Home'
import LoginButton from './Components/LoginButton'
import {Route, Routes} from 'react-router-dom'

function App() {

  return (
    
    <div className="App">
      <>
        <Navbar/>
        <div>
          <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/search" element={<Search/>}/>
            <Route path="/coursecart" element={<CourseCart/>}/>
            <Route path="/about" element={<About/>}/>
          </Routes>
        </div>
      </>
    
      <LoginButton/>

    </div>   
  );
}

export default App;