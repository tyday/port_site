import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";
const Table = ({ data }) =>
  !data ? (
    <p>Nothing to show</p>
  ) : (
    <div className="column">
      <table>
          <tbody>
          <tr>
              <td>Time</td>
              <td>{data.timestamp ? data.timestamp : 'null'}</td>
          </tr>
          <tr>
              <td>Temp</td>
              <td>{data.temperature.value ? (data.temperature.value *9/5 +32).toFixed(1) : 'null'}&#0176;F</td>
          </tr>
          <tr>
              <td>Humidity</td>
              <td>{data.relativeHumidity.value ? data.relativeHumidity.value.toFixed(0) : 'null'}%</td>
          </tr>
          <tr>
              <td>Pressure</td>
              <td>{data.barometricPressure.value ? (data.barometricPressure.value/100) : 'null'} hPa</td>
          </tr>
          <tr>
              <td>Wind Direction</td>
              <td>{data.windDirection.value ? data.windDirection.value.toFixed(0) : 'null'}</td>
          </tr>
          <tr>
              <td>Wind Speed</td>
              <td>{data.windSpeed.value ? (data.windSpeed.value * 2.237 ).toFixed(0) : "null"}</td>
          </tr>
          <tr>
              <td>Metar</td>
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