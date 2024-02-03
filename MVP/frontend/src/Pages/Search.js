import SearchPageList from '../Components/SearchPageList.js'
import searchResult from '../Components/DataTest.json'
import "../Styles/Pages.css"

export default function Course(){
    console.log(searchResult)
    return (
        
            <SearchPageList results={searchResult}/> 
        
    
    )
}