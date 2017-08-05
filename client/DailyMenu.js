import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';

function Menu(props) {
  const linkUrl = "/order/" + props.menu.id;
  const price_chf = "CHF " + props.menu.price

  return (
    <div key={props.menu.id}>
      <li>
        <h3>{props.menu.name}</h3>
        <Link to={linkUrl}>
          <li className="menu-container">
            <img className="image" src={props.menu.image} alt='menu' height='400' width='400' />
            <div className="overlay">
              <div className="text">{props.menu.description}</div>
            </div>
          </li>
        </Link>
        <h3>{price_chf}</h3>
      </li>
    </div>
  )
}

class DailyMenu extends Component {
  constructor(props) {
    super(props);
    this.handleClick = this.handleClick.bind(this)
  }

  handleClick(props) {
    //
  }

  componentDidMount() {
    //api calls
    console.log(this.props)
  }

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Daily Menu</h2>
        </div>
        <ul className='menu-items'>
          {this.props.menus &&
            this.props.menus.map(menu => {
               return <Menu menu={menu} />
            })
          }
        </ul>
      </div>
    );
  }
}

export default DailyMenu;
