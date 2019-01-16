import React, {Component} from 'react'
import {Container,Row} from 'reactstrap'
import {Redirect} from 'react-router-dom'

export default class Home extends Component {

    constructor(props) {
        super(props)
        this.state = {
            currentUser: JSON.parse(localStorage.getItem('currentUser'))
        }
    }

    logout = (e) => {
        localStorage.removeItem('jwt')
        localStorage.removeItem('currentUser')
        this.forceUpdate()
    }

    render(){
        const {currentUser} = this.state
        
        if (localStorage.getItem('jwt')) {
            return(    
                <section className="h-100" id="dashboard"> 
                    <h1>Hello</h1>
                    <button onClick={this.logout}>Log out</button>
                </section>
            )
        }
        else{
            return <Redirect to='/login'/>;
        }

    }
}


