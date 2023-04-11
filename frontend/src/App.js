import React from "react";
import './index.css'; 
import SideBar from "./components/SideBar";
import SubContent from "./components/SubContent";
import Content from "./components/Content";



function App() {

  


  return (
    <div className="flex flex-row h-screen p-4 w-screen bg-blue-100">
    <SideBar />
    <SubContent />
    <Content/>
  
    </div>
  );
}



export default App


