import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewSweatshirtForm extends React.Component {
  state = {
    pk: 0,
    brand: "",
    model: "",
    gender: "",
    price: "",
    description:"",
    image:""
  };

  componentDidMount() {
    if (this.props.sweatshirt) {
      const { pk, brand, model, gender, price,description,image } = this.props.sweatshirt;
      this.setState({ pk, brand, model, gender, price,description,image});
    }
  }

  onChange = e => {
    this.setState({ [e.target.brand]: e.target.value });
  };

  createSweatshirt = e => {
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editSweatshirt = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.sweatshirt ? this.editSweatshirt : this.createSweatshirt}>
        <FormGroup>
          <Label for="name">Name:</Label>
          <Input
            type="text"
            name="name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.name)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="name">Price:</Label>
          <Input
            type="number"
            name="price"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.price)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="description">Description:</Label>
          <Input
            type="text"
            name="description"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.description)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="image">Image:</Label>
          <Input
            type="text"
            name="image"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.image)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewSweatshirtForm;