import React, {useState } from 'react'

import { HiUserCircle } from "react-icons/hi2";
import { SlMagnifier } from "react-icons/sl";
import { SlMenu } from "react-icons/sl";
import { AiOutlineArrowUp } from "react-icons/ai";
import { FaMusic } from "react-icons/fa";


const Content = () => {


  const [artist, setArtist] = useState(null);
  const [lyrics, setLyrics] = useState("");

  async function handleSubmit(e) {
    e.preventDefault()

    fetch(`/${artist}`).then(
      res => res.json()
    ).then(
      data => {
        setLyrics(data.lyric)
      }
      
    )

  }

  return (
    <div className="flex flex-col m-1 w-3/4">
      <div className="flex flex-row w-full p-4 items-center h-1/6">
        <FaMusic  size='4em' color="gray"/>
        <p className="mx-4 text-xl font-bold">Lyric Generator</p>
        <SlMagnifier  size='2em' color="gray" className="fixed right-28"/>   
        <SlMenu  size='2em' color="gray" className="fixed right-12"/>
      </div>
      <div className="bg-blue-200 flex flex-col h-5/6 rounded-3xl p-4 px-8 w-full">
      <div className="flex flex-row fixed bottom-10 items-center w-3/4">
        {/* <input type="text" name="name" placeholder="Search" className="rounded-xl p-3 w-3/4 mx-4"/> */}
        <form onSubmit={handleSubmit}>
        <select 
          id="artist"
          onChange={(e) => setArtist(e.target.value)}
          defaultValue={'Ed Sheeran'}
          className="rounded-xl p-3 w-3/4 mx-4">
          <option value="edsheerean">Ed Sheeran</option>
          <option value="taylor">Taylor Swift</option>
          <option value="eminem">Eminem</option>
          <option value="coldplay">ColdPlay</option>
        </select>
        
        <div className="hover:bg-green-300 rounded-2xl p-2 bg-blue-300 px-2">
          <button>
          <AiOutlineArrowUp  size='2em' color="white"/>
          </button>
        </div>
        </form>
        
      </div>
      <p className="m-5 text-md">{lyrics ? lyrics : "loading"}</p>
      </div>
    </div>
  )
}

export default Content

