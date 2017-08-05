import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';
import './App.css';

class Nav extends Component {
  render() {
    return (
      <ul className='nav'>
        <li>
          <NavLink exact activeClassName='active' to='/'>
            Home
          </NavLink>
        </li>
        <li>
          <NavLink exact activeClassName='active' to='/dailymenu'>
            DailyMenu
          </NavLink>
        </li>
        <li>
          <NavLink exact activeClassName='active' to='/order'>
            Order
          </NavLink>
        </li>
      </ul>
    );
  }
}

export default Nav;
