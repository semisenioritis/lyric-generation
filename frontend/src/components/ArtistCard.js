import React from 'react'
import { HiUserCircle } from "react-icons/hi2";

const ArtistCard = ({ artistName }) => {
  return (
    <div className="bg-gray-900 h-1/6 my-2 rounded-xl flex flex-row items-center p-3 transition ease-in-out delay-150 hover:-translate-y-1 hover:scale-110 hover:bg-blue-300 duration-300 hover:text-gray-800">
        <div className="mr-2"> 
          <HiUserCircle  size='4em' color="gray"/>
        </div>
        <div className="flex flex-col">
          <div className="flex flex-row justify-between mb-2 text-sm">
            <p className='text-white font-bold'>{ artistName }</p>
            <p className='text-white'>2022-2-11</p>
          </div>
          <p className="text-sm text-gray-400 "> is simply dummy text of the printing and typesetting industry. Lorem Ipsum has,</p>  
        </div>
      </div>
  )
}

export default ArtistCard