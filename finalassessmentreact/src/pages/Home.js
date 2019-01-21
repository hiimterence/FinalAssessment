import React, {Component} from 'react'
import {Redirect} from 'react-router-dom'
import SideNavbar from '../components/Navbar'
import HelperFinder from './HelperFinder'

export default class Home extends Component {

    constructor(props) {
        super(props)
        this.state = {
            currentUser: JSON.parse(localStorage.getItem('currentUser'))
        }
    }

    

    render(){
        
        if (localStorage.getItem('jwt')) {
            return(  
                    <section className="h-100" id="dashboard">
                        <SideNavbar/>
                        <HelperFinder/>
                        <h1 className="welcome">Hello There {localStorage.getItem('userFirstName')}  {localStorage.getItem('userLastName')}!  Welcome to MyHelpers. <br/>Here are some available helpers</h1>
                        
                    </section>
            )
        }
        else{
            return <Redirect to='/login'/>;
        }

    }
}


