import React, { useState } from "react";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import "../Styles/SearchPageList.css";


export default function Filter({ courses, setCourses, setSubjectCodes, subjectCodes }) {
    const [allCourses, setAllCourses] = useState(courses);
    const [subjectCode, setSubjectCode] = useState('');

    const filterItem = (target) => {
        const newList = allCourses.filter((course) => course.subject_code === target);
        setCourses(newList);
    };

    const handleChange = (event) => {
        const target = event.target.value;
        setSubjectCode(target);

        if (target === "All") {
            showAll();
        } else {
            filterItem(target);
        }
    };

    const showAll = () => {
        setCourses(allCourses);
    };

    return (
        <div className="filter">
            <FormControl sx={{ m: 1, minWidth: 120, backgroundColor: 'white' }} size="small">
                <InputLabel id="filter-select-label">Filter</InputLabel>
                <Select
                    labelId="filter-select-label"
                    id="filter-select"
                    value={subjectCode}
                    label="Filter"
                    onChange={handleChange}
                >
                    <MenuItem value="All">All Departments</MenuItem>
                    {subjectCodes.map((code, index) => (
                        <MenuItem key={index} value={code}>
                            {code}
                        </MenuItem>
                    ))}
                </Select>
            </FormControl>
        </div>
    );
}
