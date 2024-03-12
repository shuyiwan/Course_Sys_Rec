import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom'; 
import '../Styles/CourseCart.css'; 
import testData from '../Components/DataTest.json';
import CourseCartItem from '../Components/CourseCartItem';
import emptyCartIcon from '../assets/empty-cart.png';
import actionIcon from '../assets/action.png';
import "../Styles/YoutubeVideo.css";
import YoutubeVideoList from '../Components/YoutubeVideoList.js';

export default function CourseCart() {

    const [cartItems, setCartItems] = useState([]);
    const [videoData, setVideoData] = useState([]);
    const [currentCourse, setCurrentCourse] = useState('');
    const [showStatus, setShowStatus] = useState(false);

    async function getCourseList() {
        const response = await fetch(`https://intermittence.pythonanywhere.com/shoppingCart/retrieve/?email=` + localStorage.getItem("email"), {
            credentials: 'include',
        });
        const data = await response.json();
        console.log(data);
        setCartItems(data);
    }

    useEffect(() => {
        //http://127.0.0.1:8000/shoppingCart/retrieve/?email=test@ucsb.edu
        //setCartItems(testData);
        getCourseList();
       
    }, [localStorage.getItem("loginStatus")])

    async function removeItem(index) {
        const updatedCart = [...cartItems];
        updatedCart.splice(index, 1);
        setCartItems(updatedCart);
        let ID = cartItems[index].courseID
        let sqlID = cartItems[index].sql_id
        // ID = ID.replace(/\s/g, '')
        console.log(ID)
        //http://127.0.0.1:8000/shoppingCart/delete/?email=test@ucsb.edu&courseID=CS148
        const response = await fetch('https://intermittence.pythonanywhere.com/shoppingCart/delete/?email='
            + localStorage.getItem("email") + '&courseID=' + ID + '&sql_id=' + sqlID, {
            method: 'GET',
        });
        const data = await response.json();
        //console.log(data)
        //getCourseList();
    }

    if (localStorage.getItem("loginStatus") === "false" || localStorage.getItem("loginStatus") === null){
        return (
            <div style={{ textAlign: 'center', marginTop: '50px' }}> 
                <h1>Please login to view your cart</h1>
                <img src={actionIcon} alt="Action Icon" className="iconAction" /> 
            </div>
        );
    }
    
    else {
        if (cartItems.hasOwnProperty("Empty")) {
            return (
                // need someone to work on the css for this message 
                <div> 
                    <div className="emptyCartContainer">
                        <img src={emptyCartIcon} alt="The cart is empty" style={{ maxWidth: '120px' }}/>
                        <p className="NothingInCart">Nothing in the cart...</p>   
                    </div>
                    <div className="searchButtonContainer">
                        <Link to="/" className="searchButton">Back to Search</Link>
                    </div>
                </div>
                
            )
        }
        else{ 
            const updateVideoData = (newData, newID, newShowState) => {
                setVideoData(newData);
                setCurrentCourse(newID);
                setShowStatus(newShowState);
            };

            const handleClick = () => {
                setShowStatus(false);
              };

            return (
                <div>
                    <div id="shopping-cart">
                        {cartItems.map((course, id) => (
                            <CourseCartItem 
                            course={course} id={id} 
                            removeItem={removeItem} 
                            updateVideoData={updateVideoData}/>
                        ))}
                    </div> 
    
                    <div className="searchButtonContainer">
                        <Link to="/" className="searchButton">Back to Search</Link>
                    </div>

                    {showStatus && <div>
                        <button className='close-youtube-button' onClick={handleClick}>✖️</button>
                        <YoutubeVideoList videos={videoData} currentCourse={currentCourse}/>
                    </div>}
                </div>
            );
        }        
    }
}
