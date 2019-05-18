import React from 'react'
import "../styles/AreaForecastDiscussion.css"

export default function AreaForecastDiscussion(props) {
    const afdList = props.afd.split("\n")
    // console.log(afdList)
  return (
    <div className="text-content">
      {afdList.map((value,index)=>{
          return <p key={index}>{value}</p>
      })}
    </div>
  )
}
