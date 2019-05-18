import React from 'react'

export default function AreaForecastDiscussion(props) {
    const afdList = props.afd.split("\n")
    // console.log(afdList)
  return (
    <div>
      {afdList.map((value,index)=>{
          return <p key={index}>{value}</p>
      })}
    </div>
  )
}
