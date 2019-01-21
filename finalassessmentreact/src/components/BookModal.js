import React,{Component} from 'react'
import { Alert, Button, Form, FormGroup, Input, Label, Col, Modal, ModalBody, ModalFooter, ModalHeader } from 'reactstrap'


export default class BookModal extends Component {
    constructor(props) {
        super(props)
        this.state = {
        }
      }

    render(){
        return(
            <div>
                <Col md="10" className="ml-sm-auto p-0">
                    <Modal className={this.props.className}>
                        <ModalHeader >Enter your payment details</ModalHeader>
                        <ModalBody>
                            <Label></Label>
                            <div style={{ 'float': 'right' }}>
                                <Button color="primary">Place Bid</Button>{' '}
                                <Button color="secondary">Cancel</Button>
                            </div>
                        </ModalBody>
                        <ModalFooter>
                            <div><small> You are one step away from completing your bid! No funds will be deducted until the bid closes with you as the highest bidder.</small></div>
                        </ModalFooter>
                    </Modal>

                </Col>
            </div>
        )    
    }
}