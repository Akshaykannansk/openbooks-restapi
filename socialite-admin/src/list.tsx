import React, { useState, useEffect } from "react";


function List(){
  const url = "http://10.0.0.87:8000/user/user-list";
  const [data, setData] = useState([]);

  const fetchInfo = () => {
    return fetch(url)
      .then((res) => res.json())
      .then((d) => setData(d))
    }
    useEffect(() => {
      fetchInfo();
    }, []);

  
    return(<>
      <table className="table table-responsive">
        <thead className="thead-dark">
          <tr>
            <th scope="col">ID</th>
            <th scope="col">Username</th>
            <th scope="col">First Name</th>
            <th scope="col">Last Name</th>
            <th scope="col">Email</th>
          </tr>
        </thead>
        <tbody>
          {data.map((dataObj:any, index) => {
            return (
              <tr key={dataObj.id}>
                <th scope="row">{dataObj.id}</th>
                <td>{dataObj.username}</td>
                <td>{dataObj.first_name}</td>
                <td>{dataObj.last_name}</td>
                <td>{dataObj.email}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </>
    )
  } 
  export default List
