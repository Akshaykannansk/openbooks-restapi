import React, { useState } from 'react';
import Header from './headder';
import ToastComponent  from "./toster"

const RegistrationForm = () => {
  const [formData, setFormData] = useState({
    username: '',
    first_name:'',
    last_name:'',
    email: '',
    password: '',
  });
  const [reg_stat,setreg_stat]=useState(false)
  const [bad,setbad]=useState(false)
  const [message,setmessage]=useState('')
  const [showToaster, setShowToaster] = useState(false);
  const handleChange = (e:any) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e:any) => {
    
    e.preventDefault();
    // Handle form submission (e.g., send data to a server, validate, etc.)
    fetch('http://10.0.0.87:8000/user/register',{
      method:'POST',
      headers:{"content-type": "application/json"},
      body:JSON.stringify(formData)
    }).then((res)=>{
      {if (res.status==201){
        setreg_stat(true)
      }else if(res.status== 400){
        setbad(true)
        }}
        return res.json()

    })
    .then((data) => {
      // log JSON data
      // data.map((item:any)=>{
      //   setmessage(item)
      // })
      setmessage(data['username'])
      setShowToaster(true);
    console.log(data['username'],'---data');
  });
    // console.log(formData);

  };

  return (<>
  {message &&  <ToastComponent message={message}/> }
  {!reg_stat &&
    <div className="container d-flex justify-content-center align-items-center vh-100">
      <div className="card">
        <div className="card-body">
          <h2 className="card-title">Registration Form</h2>
          <form onSubmit={handleSubmit}>
          <div className="mb-3">
              <label htmlFor="first_name" className="form-label">
                First Name
              </label>
              <input
                type="text"
                name="first_name"
                id="first_name"
                className="form-control"
                value={formData.first_name}
                onChange={handleChange}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="last_name" className="form-label">
                Last Name
              </label>
              <input
                type="text"
                name="last_name"
                id="last_name"
                className="form-control"
                value={formData.last_name}
                onChange={handleChange}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="username" className="form-label">
                Username
              </label>
              <input
                type="text"
                name="username"
                id="username"
                className="form-control"
                value={formData.username}
                onChange={handleChange}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="email" className="form-label">
                Email
              </label>
              <input
                type="email"
                name="email"
                id="email"
                className="form-control"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="password" className="form-label">
                Password
              </label>
              <input
                type="password"
                name="password"
                id="password"
                className="form-control"
                value={formData.password}
                onChange={handleChange}
                required
              />
            </div>
            <div className="d-flex justify-content-center">
              <button type="submit" className="btn btn-primary">
                Register
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  }
  {reg_stat &&<>
 <div className="container d-flex justify-content-center align-items-center vh-100">
 <div className="card">
   <div className="card-body">
     <h2 className="card-title">Registration Successful</h2>
     <div className="d-flex justify-content-center">
              <a href="/login">
              <button type="submit" className="btn btn-primary">
                Login
              </button>
              </a>
            </div>

     </div>
      </div>
    </div>
    </>
  }
    </>
  );
};

export default RegistrationForm;
