import React,{Component} from 'react';
import {Container,Row} from 'reactstrap'
import {Redirect} from 'react-router-dom'
import Axios from 'axios';
import SideNavbar from '../components/Navbar'
import {Button} from 'reactstrap'

export default class HelperFinder extends Component {
    constructor(props) {
        super(props)
        this.state = {
           all_maids:[]
        }
    }

    pay = () =>{
        console.log('hello')
    }

    componentDidMount = () =>{
        Axios.get('http://localhost:5000/api/v1/maids')
        .then(response =>{
            console.log(response)
            this.setState({all_maids:response.data.all_maids})
        })
        .catch(error =>{
            console.log(error)
        })
    }
  render(){
        if (localStorage.getItem('jwt')) {
            return(
                <div>
                    <SideNavbar/>
                    <div>
                    <section className="h-100" > 
                        <Container fluid className="h-100">
                            <Row className="h-100">
                            </Row>
                        </Container>
                    </section>
                    <section id='maidcontainer'>
                        <div>
                    {
                        this.state.all_maids.map((maid,index)=>
                        <div onClick={this.onClickHandler} className='maid' id={index} key={index}>
                            
                            <img src={maid.image} alt='hello' className='maidphoto'/>
                            Name : {maid.name}<br/>
                            Age : {maid.age}<br/>
                            Country : {maid.country} <br/>
                            <Button className="btn btn-dark" value="Submit">
                                Interested? Book a session to meet
                            </Button>
                            
                            <hr/>
                            
                        </div>
                        )
                    }
                    </div>
                    
                    </section>
                    </div>
                </div>
            )
        }
        else{
            return <Redirect to='/login'/>;
        }
    }
}