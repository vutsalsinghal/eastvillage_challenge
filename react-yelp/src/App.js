import React, { Component } from 'react';
import {BrowserRouter, Route, Switch } from 'react-router-dom';
import Layout from './components/Layout';
import Home from './components/Home';
import eventDetail from './components/eventDetail';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Layout>
          <Switch>
            <Route exact path="/eastvillage_challenge" component={Home} />
            <Route path="/eastvillage_challenge/eventDetail/:id/:miles_away" component={eventDetail} />
          </Switch>
        </Layout>
      </BrowserRouter>
    );
  }
}

export default App;