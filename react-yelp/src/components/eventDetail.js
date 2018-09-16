import React, { Component } from 'react';
import {Button, Card, Grid, Loader, Dimmer} from 'semantic-ui-react';
import axios from 'axios';
import GoogleMapReact from 'google-map-react';

class eventDetail extends Component{
  state = {
    loadingData:false,
    detail:'',
    zoom:14,
  }

  async componentDidMount(){
    this.setState({loadingData:true});
    document.title = "EastVillage | Event Detail";

    var config = {};

    const url = 'https://eastvillage.pythonanywhere.com/json/event_detail/' + this.props.match.params.id + '&' + this.props.match.params.miles_away
    let response = await axios.get(url,config);
    this.setState({detail:response.data.detail});
    this.setState({loadingData:false});
  }

  render(){
    if(this.state.loadingData){
      return (
          <Dimmer active inverted>
            <Loader size='massive'>Loading...</Loader>
          </Dimmer>
      );
    }

    return (
      <Grid stackable>
        <Grid.Column width={10}>
          <Card fluid>
            <Card.Content>
              <Card.Header>{this.state.detail.name}</Card.Header>
              <Card.Meta style={{float:'right'}}>Time: {this.state.detail.time_start}</Card.Meta>
              <Card.Meta>Cost: {this.state.detail.cost}</Card.Meta>
              <p><b>Description:</b> {this.state.detail.description}</p>
              <Button style={{float:'right'}} primary basic href={this.state.detail.event_site_url} target='_blank'>Site Link</Button>
            </Card.Content>
          </Card>
        </Grid.Column>
        <Grid.Column width={6}>
          <div style={{height:'24em', width:'24em'}}>
            <GoogleMapReact
              bootstrapURLKeys={{ key:'AIzaSyC0dv2oxK00V51-FVp7UPrmK3kAxft6PEU'}}
              defaultCenter={{lat:this.state.detail.latitude, lng: this.state.detail.longitude}}
              defaultZoom={this.state.zoom}
            >
              
            </GoogleMapReact>
          </div>
        </Grid.Column>
      </Grid>
    );
  }
}

export default eventDetail;