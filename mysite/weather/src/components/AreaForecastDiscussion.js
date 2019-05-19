import React from "react";
import "../styles/AreaForecastDiscussion.css";

export default function AreaForecastDiscussion(props) {
  function showAFD(e) {
    console.log(e.target);
    var iAm = e.target;
    var content = iAm.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  }
  const afdList = props.afd.split("\n");
  // console.log(afdList)
  return (
    <div className="text-content">
      <button onClick={showAFD} className="collapsible">
        Open AFD
      </button>
      <div style={{display:"none"}}>
        {afdList.map((value, index) => {
          return <p key={index}>{value}</p>;
        })}
      </div>
    </div>
  );
}
