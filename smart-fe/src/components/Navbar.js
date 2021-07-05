import React, { Component } from 'react';


class Navbar extends Component {
    render() {
      return (
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#news">Bags</a></li>
            <li><a href="#contact">Jeans</a></li>
            <li ><a class="active" href="#about">Shoes</a></li>
            <li ><a class="active" href="#about">Sweatshirt</a></li>
            <li ><a class="active" href="#about">T-shirt</a></li>

      </ul>
      
      );
    }
  }
  
  export default Navbar;