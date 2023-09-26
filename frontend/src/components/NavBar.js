import React from "react";
import { Navbar, Container, Nav } from "react-bootstrap";
import pflogo from '../assets/pflogo.PNG';
import styles from '../styles/NavBar.module.css';
import { NavLink } from "react-router-dom";

const NavBar = () => {
  return (
    <Navbar className={styles.NavBar} expand="md" fixed="top">
      <Container>
        <NavLink to="/">
          <Navbar.Brand>
            <img src={pflogo} alt="logo" height="50" />
          </Navbar.Brand>
        </NavLink>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ml-auto">
            <NavLink 
            to="/" 
            exact 
            className={styles.NavLink} 
            activeClassName={styles.Active}
            >
              <i className="fa-solid fa-house"></i>Home
            </NavLink>
            <NavLink 
            to="/signin" 
            className={styles.NavLink} 
            activeClassName={styles.Active}
            >
              <i className="fa-solid fa-arrow-right-to-bracket"></i>Sign in
            </NavLink>
            <NavLink 
            to="/signup" 
            className={styles.NavLink} 
            activeClassName={styles.Active}
            >
              <i className="fa-solid fa-user-plus"></i>Sign up
            </NavLink>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default NavBar;
