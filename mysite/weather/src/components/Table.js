import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";


const Table = ({ data }) =>
  !data ? (
    <p>Nothing to show</p>
  ) : (
    <div className="column">
      <table>
        <thead><tr><th colSpan='2'>Current Conditions</th></tr></thead>
          <tbody>
          <tr>
              <th>Time</th>
              <td>{data.timestamp ? Date(data.timestamp).toLocaleString() : 'null'}</td>
          </tr>
          <tr>
              <th>Temp</th>
              <td>{data.temperature.value ? parseFloat((data.temperature.value *9/5 +32)).toFixed(1) : 'null'}&#0176;F</td>
          </tr>
          <tr>
              <th>Humidity</th>
              <td>{data.relativeHumidity.value ? parseFloat(data.relativeHumidity.value).toFixed(0) : 'null'}%</td>
          </tr>
          <tr>
              <th>Pressure</th>
              <td>{data.barometricPressure.value ? (data.barometricPressure.value/100) : 'null'} hPa</td>
          </tr>
          <tr>
              <th>Wind Direction</th>
              <td>{data.windDirection.value ? parseFloat(data.windDirection.value).toFixed(0) : 'null'}&#0176;</td>
          </tr>
          <tr>
              <th>Wind Speed</th>
              <td>{data.windSpeed.value ? parseFloat(data.windSpeed.value * 0.621 ).toFixed(0) : "null"} mph</td>
          </tr>
          <tr>
              <th>Metar</th>
              <td>{data.rawMessage}</td>
          </tr>
          </tbody>
      </table>
    </div>
  );
Table.propTypes = {
  data: PropTypes.object.isRequired
};
export default Table;