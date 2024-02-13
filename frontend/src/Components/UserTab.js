import React, { useState } from 'react';
import '../Styles/DropdownTab.css';

const UserTab = ({myprofile, logOut}) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleClick = () => {
    logOut();
  };

  const handleMouseEnter = () => {
    setIsOpen(true);
  };

  const handleMouseLeave = () => {
    setIsOpen(false);
  };

  return (
    <div className="dropdown-container"
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}>
      <button className="dropdown-button">
        <img src={myprofile.picture} alt="user pic" className="round-image small-image" />
        Hi, {myprofile.name}!
      </button>
      {isOpen && (
        <div className="dropdown-content">
          <button onClick={handleClick}>Log Out</button>
        </div>
      )}
    </div>
  );
};

export default UserTab;
