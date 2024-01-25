import ReactSearchBox from 'react-search-box'

export default function Home(){
    const columns = [
        {
          key: "john",
          value: "John Doe",
        },
        {
          key: "jane",
          value: "Jane Doe",
        },
        {
          key: "mary",
          value: "Mary Phillips",
        },
        {
          key: "robert",
          value: "Robert",
        },
        {
          key: "karius",
          value: "Karius",
        },
      ];
      
    return (
        <div>
            <h1>Home Page Not Implemented yet</h1>
            <p className='searchBarContainer'>
            <ReactSearchBox
                placeholder="Search a course name"
                value="Doe"
                data={columns}
                callback={(record) => console.log(record)}
            />
        </p>
        </div>
        


    )
}