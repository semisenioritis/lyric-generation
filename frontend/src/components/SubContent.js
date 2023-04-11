import React, { useState } from 'react'
import ArtistCard from './ArtistCard'

const SubContent = () => {

  


  return (
    <div className="flex flex-col m-1 p-5 w-1/4">

    <p className="text-gray-800 mb-2 text-lg font-bold ml-1">Supported Artists</p>
    <input type="text" name="name" placeholder="Search" className="rounded-xl p-2 hover:border-fuchsia-300 border-2 sele:border-fuchsia-300 h-12 mb-3"/>

    <p className="text-gray-800 mb-2 text-lg font-bold ml-1">Recent Artist queries:</p>
    <ArtistCard artistName={'Ed Sheeran'}/>
    <ArtistCard artistName={'Taylor Swift'}/>
    <ArtistCard artistName={'Eminem'}/>
    <ArtistCard artistName={'coldPlay'}/>
    

  </div>
  )
}

export default SubContent