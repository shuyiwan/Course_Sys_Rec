import SearchPageList from '../Components/SearchPageList.js'
import { useLocation } from 'react-router-dom';
//import searchResult from '../Components/DataTest.json'
//import { saveAs } from 'file-saver';
import "../Styles/Pages.css"

export default function Course(){
    let location = useLocation();
    let resultFromSearchBar = location.state.jsonFile
    const isJsonEmpty = Object.keys(resultFromSearchBar).length === 0;
    console.log(isJsonEmpty)
    
    if(isJsonEmpty){
        return (
            <div classname>
                No such courses bro!
            </div> 
        )
    }

    else{
        return (
            <SearchPageList results={resultFromSearchBar}/> 
        )
    }

    
}