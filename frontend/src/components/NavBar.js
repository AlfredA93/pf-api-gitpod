import React from "react";
import { Navbar, Container, Nav } from "react-bootstrap";
import pflogo from '../assets/pflogo.PNG'

const NavBar = () => {
  return (
    <Navbar expand="md" fixed="top">
      <Container>
        <Navbar.Brand><img src={pflogo} alt="logo" height="50" /></Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto">
            <Nav.Link><i className="fa-solid fa-house"></i>Home</Nav.Link>
            <Nav.Link><i className="fa-solid fa-arrow-right-to-bracket"></i>Sign in</Nav.Link>
            <Nav.Link><i className="fa-solid fa-user-plus"></i>Sign up</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;