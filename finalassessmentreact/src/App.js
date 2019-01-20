import React, { Component, Fragment } from 'react';
import './App.scss';
import Home from './pages/Home'
import Login from './pages/Login'
import SignUp from './pages/SignUp'
import {Route, Switch} from 'react-router-dom'
import HelperFinder from './pages/HelperFinder'
import SideNavbar from './components/Navbar';

class App extends Component {

  constructor(props) {
    super(props)
    this.state = {
    }
  }

  render(){
    return (
      

      <Fragment>

        <div className = "content">
          <Switch>
            <Route path="/login" 
              component = { props => 
                      {
                        return (
                          <Login 
                            {...props}
                          />
                        )
                      }
              }
            />
            <Route path="/home" 
              component = { props => 
                      {
                        return (
                          <Home
                            {...props}
                          />
                        )
                      }
              }
            />
            <Route path="/signup" 
              component = { props => 
                      {
                        return (
                          <SignUp 
                            {...props}
                          />
                        )
                      }
              }
            />    
            <Route path="/maids"
              component = { props => 
                      {
                        return (
                          <HelperFinder 
                          {...props}
                          />
                        )
                      }
              }
            />
 
          </Switch>
        </div>
      </Fragment>
    )
  }
}

export default App;
