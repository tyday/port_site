import React, { Component } from "react";
import PropTypes from "prop-types";
import AreaForecastDiscussion from "./AreaForecastDiscussion"

class DataProvider extends Component {
  static propTypes = {
    endpoint: PropTypes.string.isRequired,
    render: PropTypes.func.isRequired
  };
  state = {
    data: [],
    loaded: false,
    placeholder: "Loading...",
    afd:'Loading...'
  };
  location = {
    latitude:0,
    longitude:0,
    city:""
  }
  
  autofillObservations(data){
    const humidity = document.getElementById('id_observed_outdoor_humidity')
    const temp = document.getElementById('id_observed_outdoor_temperature')
    const pressure = document.getElementById('id_observed_pressure_millibars')
    const latitude = document.getElementById('id_latitude')
    const longitude = document.getElementById('id_longitude')
    const city = document.getElementById('id_city')
    const state = document.getElementById('id_state')
    if(humidity){
      latitude.value = this.location.latitude.toFixed(4)
      longitude.value = this.location.longitude.toFixed(4)
      city.value = this.location.city
      state.value = this.location.state
      // console.log(data)
      // humidity.innerHTML = data.
      humidity.value = Math.round(data.relativeHumidity.value)
      temp.value = Math.round(data.temperature.value *9/5+32)
      pressure.value = Math.round(data.barometricPressure.value/100)
    }
  }
  getAreaForecastDiscussion(office){
      var afdUrl = `https://api.weather.gov/products/types/afd/locations/${office}`
    //   console.log(afdUrl)
      fetch(afdUrl)
      .then(response => {
        if (response.status !== 200) {
          return this.setState({ afd: "Something went wrong" });
        }
        return response.json()
      })
      .then(response =>{
        //   console.log(response["@graph"][0]["@id"])
        afdUrl = response["@graph"][0]["@id"]
        fetch(afdUrl)
        .then(response => {
            if (response.status !== 200) {
              return this.setState({ afd: "Something went wrong" });
            }
            return response.json()
          })
          .then(response => {
              this.setState({afd:response.productText})
          })
      })
      
  }
  populateData() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(position => {
        var { latitude, longitude } = position.coords;
        this.location = { latitude, longitude }
        const weatherUrl = `https://api.weather.gov/points/${latitude.toFixed(4)},${longitude.toFixed(4)}`;
        // console.log(weatherUrl);
        fetch(weatherUrl)
          .then(response => {
            if (response.status !== 200) {
              return this.setState({ placeholder: "Something went wrong" });
            }
            return response.json();
          })
          .then(response => {
              this.getAreaForecastDiscussion(response.properties.cwa)
              // console.log('79: ', response)
              // console.log('82', response.properties.relativeLocation.properties.city)
              this.location['city'] = response.properties.relativeLocation.properties.city
              this.location['state'] = response.properties.relativeLocation.properties.state
              // console.log(this.location)
            // console.log(response.properties.observationStations);
            fetch(response.properties.observationStations)
              .then(response => {
                if (response.status !== 200) {
                  return this.setState({ placeholder: "Something went wrong" });
                }
                return response.json();
              })
              //     .then(response => {
              //         console.log(response)

              //     })})
              // })
              .then(response => {
                // console.log(response)
                var pollingStation = response.observationStations[0];
                pollingStation = `${pollingStation}/observations/current`;
                fetch(pollingStation)
                  .then(response => {
                    if (response.status !== 200) {
                      return this.setState({
                        placeholder: "Something went wrong"
                      });
                    }
                    return response.json();
                  })
                  .then(response => {
                    // console.log(response.properties);
                    this.setState({ data: response.properties, loaded: true });                    
                    this.autofillObservations(response.properties)
                  });
              });
          });
      });
    } else {
      this.setState({ placeholder: "Browser does not support geolocation" });
    }
  }
  componentDidMount() {
    // fetch(this.props.endpoint)
    //   .then(response => {
    //     if (response.status !== 200) {
    //       return this.setState({ placeholder: "Something went wrong" });
    //     }
    //     return response.json();
    //   })
    //   .then(data => this.setState({ data: data, loaded: true }));
    this.populateData();
  }
  render() {
    const { data, loaded, placeholder,afd } = this.state;
    if (loaded){
        return(
            <div>
                {this.props.render(data)}
                <AreaForecastDiscussion afd={afd} />

            </div>
        )
    } else {
        return <p>{placeholder}</p>
    }
//     return loaded ? this.props.render(data) : <p>{placeholder}</p>;
//   }
}}
export default DataProvider;
