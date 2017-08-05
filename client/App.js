import React, { Component } from 'react';
import './App.css';
import Welcome from './Welcome';
import DailyMenu from './DailyMenu';
import Nav from './Nav';
import Order from './Order';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { getAllMenus } from './utils/api';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      menus: [],
    }
  }

  componentDidMount() {
   getAllMenus().then(response => {
        console.log(response)
        this.setState({menus: response});
      });
  }

  render() {
    return (
      <Router>
        <div className='container'>
          <Nav />
          <Switch>
            <Route exact path='/' component={Welcome} />
            <Route path='/dailymenu' render={(props) => <DailyMenu {...props} menus={this.state.menus} />} />
            <Route path='/order/:id' render={(props) => <Order {...props} menus={this.state.menus} />} />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
