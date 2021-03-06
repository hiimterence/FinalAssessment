import React, {Component} from 'react'
import {Link, Redirect} from 'react-router-dom'
import axios from 'axios';
import {Alert,Container,Col,Row,Form,FormGroup,Input,Button} from 'reactstrap'

export default class SignUp extends Component {
    constructor(props) {
        super(props)
        this.state = {
            email:'',
            password:'',
            firstname:'',
            lastname:'',
            message:'',
            loading:false,
            hasError:false,
            errors:[],
        }
    }

    postCredentials = (e) =>{
        e.preventDefault()
        axios({
            method: 'post',
            url: 'http://127.0.0.1:5000/api/v1/users/create',
            headers: {
                'content-type': 'application/json',
            },
            data: {
                first_name:this.state.firstname,
                last_name:this.state.lastname,
                email:this.state.email,
                password:this.state.password,
            }
          })
        .then( response => {
            // console.log(response)
            const {data} = response;
            const {message, auth_token} = data
            const user = response.data.user

            localStorage.setItem('jwt',auth_token)
            localStorage.setItem('userEmail',JSON.stringify(user.email))
            localStorage.setItem('userFirstName',JSON.stringify(user.first_name))
            localStorage.setItem('userLastName',JSON.stringify(user.last_name))
            localStorage.setItem('profilePhoto',JSON.stringify(user.profile_photo))

            this.setState({
                message:message
            })
        })
        .catch(error => {
            console.log(error)
            this.setState({errors: error.response.data.message, hasError: true})
        });    
    }

    handleEmail = (event) =>{
        const target = event.target
        const value = target.value

        this.setState({
            email : value
        })
    }

    handleFirstName = (event) =>{
        const target = event.target
        const value = target.value
        
        this.setState({
            firstname : value
        })
    }

    handleLastName = (event) =>{
        const target = event.target
        const value = target.value
        
        this.setState({
            lastname : value
        })
    }

    handlePassword = (event) =>{
        const target = event.target
        const value = target.value
        
        this.setState({
            password : value
        })
    }

    handleSubmit = (e) => {
        e.preventDefault();
    }

    render(){
        if(localStorage.getItem('jwt')){
            return <Redirect to= '/'/>
        }
        else{ 
            return(
                <section className="h-100" id="login-page">
                    <Container fluid className="h-100">
                        <Row className="h-100">
                            <Col md="7" className="h-100 d-none d-md-block" id="login-left-banner">
                                <div className="mb-auto mt-3">
                                    <h3>LOGO</h3>
                                </div>
                            </Col>
                            <Col md="5" className="h-100 d-flex align-items-start flex-column" id="login-right-banner">
                                <div className="mb-auto m-5">
                                    <h1>Sign Up</h1>
                                    <p>Hello! Let's get started by making your account!</p>
                                </div>
                                <Form className="mb-auto w-100 p-5" onSubmit={this.handleSubmit && this.postCredentials}>
                                    <FormGroup>
                                        <Input onInput={this.handleFirstName}
                                            className = "form-control border-top-0 border-left-0 border-right-0 bg-transparent" 
                                            name = "firstname" 
                                            placeholder ="First Name"
                                            required
                                        />
                                        <Alert color='primary'>Once registered, is unchangeable</Alert>
                                        <Input onChange={this.handleLastName}
                                            className = "form-control border-top-0 border-left-0 border-right-0 bg-transparent" 
                                            name = "lastname" 
                                            placeholder ="Last Name"
                                            required
                                        />
                                        <Alert color='primary' >Once registered, is unchangeable</Alert>

                                        <Input onChange={this.handleEmail}
                                            className = "form-control border-top-0 border-left-0 border-right-0 bg-transparent" 
                                            name = "email" 
                                            type='email'
                                            placeholder ="Email"
                                            required
                                        />
                                        <Alert color='primary' className='alert'>Once registered, is unchangeable</Alert>
                                        
                                        <Input onChange = {this.handlePassword}
                                            type='password'
                                            className = "form-control border-top-0 border-left-0 border-right-0 bg-transparent" 
                                            name = "password" 
                                            placeholder ="Password"
                                            required
                                        />
                                        <Alert color='primary' className='alert'>Once registered, is unchangeable</Alert>

                                        <div className="d-flex flex-row mt-3 ml-1">
                                            <Button className="btn btn-dark" value="Login">
                                                Sign Up
                                            </Button>
                                        </div>
                                    </FormGroup>
                                </Form>
                                <div>
                                    <h6>
                                    {this.state.hasError === true ? this.state.errors.map((errors,index) =>
                                    <Alert color='danger' key = {index}>{errors}</Alert>) 
                                    : ''}
                                    </h6>
                                </div>
                                <div className="mt-auto mx-auto mb-3">
                                    <small className="text-muted">
                                        Already have an account? Login &nbsp;
                                        <Link to={'/login'} className="text-muted border-bottom">
                                            here!
                                        </Link> 
                                    </small>
                                </div>
                            </Col>
                        </Row>
                    </Container>
                </section>
                )
            }
        }
    }


