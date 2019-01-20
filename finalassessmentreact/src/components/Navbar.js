import React, { Component } from 'react';
import { Col, Nav, NavItem, DropdownItem } from 'reactstrap'
import { Link } from 'react-router-dom'


export default class SideNavbar extends Component {
  constructor(props) {
    super(props)
    this.state = {
    }
  }
    logout = (e) => {
        localStorage.removeItem('jwt')
        localStorage.removeItem('currentUser')
        this.forceUpdate()
    }

  render() {
    return (
      <Col md="2" className="d-none d-md-block sidebar">
        <div className="sidebar-sticky">
          <Nav className="flex-column">
            <NavItem>
              <Link to={'/home'} className="nav-link">
                <span data-feather="home"></span>
                Home<span className="sr-only">(current)
                </span>
              </Link>
            </NavItem>
            
            <NavItem>
              <Link to={'/login'} onClick={this.logout} className="nav-link bg-transparent border-0">Log out</Link>
            </NavItem>
          </Nav>
         
        </div>
      </Col>
    )
  }

}