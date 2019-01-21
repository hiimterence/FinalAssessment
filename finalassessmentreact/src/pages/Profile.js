import React, {Component} from 'react'
import {Link, Redirect} from 'react-router-dom'
import axios from 'axios';
import {Alert,Container,Col,Row,Form,FormGroup,Input,Button,Nav,NavItem} from 'reactstrap'
import SideNavbar from '../components/Navbar';


export default class Profile extends Component {
    constructor(props) {
        super(props)
        this.state = {
            email:'',
            message:'',
            loading:false,
        }
    }

    render(){
            return(
                <div>
                    <section className="h-100" id="dashboard">
                        <SideNavbar/>
                    </section>
                    <div id='credentials'>
                        <h1>Your first name that is registered : {localStorage.getItem('userFirstName')}</h1>
                        <Alert color='primary' className='alert'>Unchangeable!</Alert>

                        <br/>
                        <br/>

                        <h1>Your last name that is registered : {localStorage.getItem('userLastName')}</h1>
                        <Alert color='primary' className='alert' >Unchangeable!</Alert>

                        <br/>
                        <br/>

                        <h1>Your email that is registered : {localStorage.getItem('userEmail')}</h1>
                        <Alert color='primary' className='alert'>Unchangeable!</Alert>

                        
                    </div>
                </div>
                )
            }
            
        }
    