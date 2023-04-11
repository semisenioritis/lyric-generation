import React from 'react'
import { HiChatBubbleLeft } from "react-icons/hi2";
import { HiUserCircle } from "react-icons/hi2";
import { AiFillHome } from "react-icons/ai";
import { AiFillStar } from "react-icons/ai";
import { BsFillBarChartFill } from "react-icons/bs";

const SideBar = () => {
  return (
    <div className="bg-gray-900 h-full rounded-2xl w-24 p-2 flex flex-col items-center py-4">

      <div className="hover:bg-blue-300 rounded-2xl mb-8 p-2">
      <AiFillHome  size='2em' color="white"/>
      </div>
      <div className="bg-blue-300 rounded-2xl mb-8 p-2">
      <HiChatBubbleLeft  size='2em' color="white"/>
      </div>
      <div className="hover:bg-blue-300 rounded-2xl mb-8 p-2">
      <AiFillStar  size='2em' color="white"/>
      </div>
      <div className="hover:bg-blue-300 rounded-2xl mb-8 p-2">
      <BsFillBarChartFill  size='2em' color="white"/>
      </div>
      <div className="hover:bg-white rounded-2xl fixed bottom-7 p-2">
      <HiUserCircle  size='3em' color="gray"/>
      </div>
      
    </div>
  )
}

export default SideBar