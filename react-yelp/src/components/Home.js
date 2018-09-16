import React, { Component } from 'react';
import {Card, Grid, Loader, Dimmer} from 'semantic-ui-react';
import axios from 'axios';

class Home extends Component {
  state = {
    loadingData:false,
    events:[],
    display_limit:'',
    total:'',
  }

  async componentDidMount(){
    this.setState({loadingData:true});
    document.title = "EastVillage Events";

    var config = {};

    let response = await axios.get('https://eastvillage.pythonanywhere.com/json/events',config);
    this.setState({events:response.data.events, total:response.data.total, display_limit:response.data.display_limit});

    this.setState({loadingData:false});
  }

  rederEvents(){
    const items = this.state.events.map((event, id) => {
      return (
        <Card key={id} fluid href={'/eastvillage_challenge/eventDetail/'+event.id+'/'+event.miles_away}>
          <Card.Content>
            <Card.Header >{event.name}</Card.Header>
            <Card.Meta style={{float:'right'}}>Time: {event.time_start}</Card.Meta>
            <Card.Meta>Cost: {event.cost}</Card.Meta>
          </Card.Content>
          <Card.Content extra>
            It's {event.miles_away} miles from you!
          </Card.Content>
        </Card>
      );
    });

    return <div>{items}</div>;
  }

  render() {
    if(this.state.loadingData){
      return (
          <Dimmer active inverted>
            <Loader size='massive'>Loading...</Loader>
          </Dimmer>
      );
    }

    return (
      <div>
        <h1>Events around East Village!</h1>
        <Grid stackable reversed="mobile">
          <Grid.Column width={12}>
            {this.rederEvents()}
            <i>Displaying {this.state.display_limit}/{this.state.total}</i>
          </Grid.Column>
          <Grid.Column width={4}>
            <Grid.Row>
            </Grid.Row>
          </Grid.Column>
        </Grid>
      </div>
    );
  }
}

export default Home;