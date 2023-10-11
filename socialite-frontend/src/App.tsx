import List from "./list";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from "./pages/home"
import Users from "./pages/users";
import Register from "./pages/register";

function app(){
  return( <Router>
  <div>
    {/* Navigation can go here */}
    
    {/* Define your routes */}
    <Routes>
      <Route path="/" element={<Home/>} />
      <Route path="/user-list" element={<Users />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  </div>
</Router>
  )
}

export default app