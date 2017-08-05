import React, { Component } from 'react';
import './App.css';

class Order extends Component {
  componentDidMount() {
    console.log(this.props)
  }

  render() {
    const menuId = Number(this.props.match.params.id);
    const menus = this.props.menus;

    return(
      <div className='order'>
        <ul>
         {menus &&
          menus.map(menu => {
            console.log(menu.id === menuId)
            if (menu.id === menuId) {
              return (
                <div>
                  <li>{menu.name}</li>
                  <li>{menu.description}</li>
                  <li>{menu.price}</li>
                </div>
              )
            }
          })}
        </ul>
      </div>
    )
  }
}

export default Order;
