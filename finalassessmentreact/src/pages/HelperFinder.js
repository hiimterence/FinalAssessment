import React,{Component} from 'react';
import {Container,Row} from 'reactstrap'
import {Redirect} from 'react-router-dom'
import Axios from 'axios';
import SideNavbar from '../components/Navbar'
import BookModal from '../components/BookModal';
import { Alert, Button, Form, FormGroup, Input, Label, Col, Modal, ModalBody, ModalFooter, ModalHeader } from 'reactstrap'
import DatePicker from 'react-datepicker'
import { setMinutes, setHours } from 'date-fns'
import { runInThisContext } from 'vm';


export default class HelperFinder extends Component {
    constructor(props) {
        super(props)
        this.state = {
           all_maids:[],
           startDate: (new Date(new Date().getTime() +86400000 *8)),
           modal: false,
           meetPlaceIsPhysical: true, 
           selectedMaidId: null,
           selectedMaidScheduledTimeToMeet:null,
           selectedMaidMeetLocation:null,
           booked_maid: false,
           maidcountryinfo:null,
           currency:[]
        }
    }

    handleChange = (date) => {
        console.log(date.getTime())
        this.setState({
            startDate: date,
            selectedMaidScheduledTimeToMeet:date
        });
    }
    
    setLocation = (e) =>{
            let target = e.target
            let value = target.value
            this.setState({
                selectedMaidMeetLocation: value
            })
    }

    toggle = (e) => {
        this.setState({
            modal: !this.state.modal,
            selectedMaidId: e.target.id
        });
    }

    generateInfo = (e) =>{
        console.log(e.target.value)
        Axios({
            method:'get',
            url:`https://restcountries.eu/rest/v2/name/${e.target.value}`
        })
        .then(response =>{
            
            this.setState({maidcountryinfo:response.data[0]})
            console.log(response.data[0])
            
        })
        
        .catch(error =>{
            console.log(error)
        })
    }
    
    convertCurrency = (e) =>{
        let currency = e.target.value

        Axios({
            method:'get',
            url:`https://api.exchangeratesapi.io/latest?symbols=${currency}&&base=MYR`
        })
        .then(response=>{
            // console.log(response.data.rates[currency])
            this.setState({currency:response.data.rates[currency]})
        })
        .catch(error =>{
            console.log(error)
        })
    }

    submit = () =>{
        Axios({
            method: 'post',
            url: 'http://127.0.0.1:5000/api/v1/bookmaid',
            headers: {
                'content-type': 'application/json',
            },
            data:{
                id:this.state.selectedMaidId,
                place_to_meet:this.state.selectedMaidMeetLocation,
                scheduled_to_meet:String(this.state.selectedMaidScheduledTimeToMeet)
            }
           
          })
        .then( response => {
            console.log(response)
            this.setState({booked_maid:true,modal: !this.state.modal})
        })
        .catch(error => {
            console.log(error)
        });    
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
                        <div className='maid' id={index + 1} key={index}>
                            
                            <img src={maid.image} alt='hello' className='maidphoto'/>
                            Name : {maid.name}<br/>
                            Age : {maid.age}<br/>
                            Country : {maid.country} <br/>
                            <Button className="btn btn-dark" onClick={this.toggle} id={index+3}>
                                Interested? Book a session to meet
                            </Button>
                            <br/>
                            Some interesting facts about their native country:
                            <Button value={maid.country} onClick={this.generateInfo}>Generate</Button>
                            <hr/>
                            
                        </div>
                        )
                    }
                    </div>
                    <div>
                        {
                            this.state.maidcountryinfo !== null
                            ?
                            <div>
                            <h1>Maid's country info:</h1>
                            <h5>
                                Capital : {this.state.maidcountryinfo.capital} <br/>
                                Currency : {this.state.maidcountryinfo.currencies[0].name} <br/>
                                Language : {this.state.maidcountryinfo.languages[0].name}
                            </h5>
                            <br/>
                            <br/>
                            <hr/>
                            </div>
                            :
                            ''

                        }
                        <Col md="10" className="ml-sm-auto p-0">
                            <Modal isOpen={this.state.modal} className={this.props.className}>
                                <ModalHeader >Enter your details</ModalHeader>
                                <ModalBody>
                                    <small>Choose a time to meet!</small>
                                    <DatePicker
                                    selected={this.state.startDate}
                                    onChange={this.handleChange}
                                    showTimeSelect
                                    timeFormat="HH:mm"
                                    injectTimes={[
                                        setHours(setMinutes(new Date(), 1), 0),
                                        setHours(setMinutes(new Date(), 5), 12),
                                        setHours(setMinutes(new Date(), 59), 23)
                                    ]}
                                    dateFormat="MMMM d, yyyy h aa"
                                    />
                                    <br/>
                                    <br/>
                                    <small>Choose a place to meet!</small>
                                    <FormGroup>
                                        <Input type="select" name="select" id="exampleSelect" onChange={this.setLocation} required>
                                        <option></option>
                                        <option>Physical(Our Office)</option>
                                        <option>Remote</option>
                                        </Input>
                                    </FormGroup>
                                    <br/>
                                    <br/>
                                    
                                    <Label></Label>
                                    <div style={{ 'float': 'right' }}>
                                        <Button color="primary" onClick={this.toggle && this.submit}>Book a session to meet</Button>{' '}
                                        <Button color="secondary" onClick={this.toggle}>Cancel</Button>
                                    </div>
                                </ModalBody>
                                <ModalFooter>
                                    <div><small>You can schedule a meeting with this person at the time and place of your choice</small></div>
                                </ModalFooter>
                            </Modal>
                        </Col>
                    </div>
                    {
                        this.state.booked_maid
                        ?
                        <Alert color='danger'>A maid has been booked! Please do not book anyone else to avoid confusion </Alert>
                        :
                        ''
                    }
                    Convert 1 Ringgit to a desired currency:
                    <Input type="select" name="select" id="exampleSelect" onChange={this.convertCurrency} required>
                        <option>HRK</option>
                        <option>HUF</option>
                        <option>IDR</option>
                        <option>TRY</option>
                        <option>RON</option>
                        <option>ISK</option>
                        <option>SEK</option>
                        <option>THB</option>
                        <option>PLN</option>
                        <option>GBP</option>
                        <option>CAD</option>
                        <option>AUD</option>
                        <option>NZD</option>
                        <option>CHF</option>
                        <option>DKK</option>
                        <option>SGD</option>
                        <option>CNY</option>
                        <option>BGN</option>
                        <option>CZK</option>
                        <option>BRL</option>
                        <option>JPY</option>
                        <option>KRW</option>
                        <option>INR</option>
                        <option>MXN</option>
                        <option>RUB</option>
                        <option>HKD</option>
                        <option>USD</option>
                        <option>ZAR</option>
                        <option>ILS</option>
                        <option>NOK</option>
                    </Input>
                    {
                        this.state.currency
                        ?
                        <h6>1 MYR = {this.state.currency}</h6>
                        :
                        ''
                    }
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