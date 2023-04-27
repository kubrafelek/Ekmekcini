import React from 'react';
import { Container } from 'react-bootstrap'
import { BrowserRouter as Router, Routes, Route, } from 'react-router-dom'
import './App.css';
import Footer from './components/Footer';
import Header from './components/Header'
import HomeScreen from './screens/HomeScreen.js';

function App() {
  return (
    <Router>
      <Header />
      <main className="py-3">
        <Container>
          <Routes>
            <Route path='/' element={<HomeScreen />} exact />
          </Routes>
        </Container>
      </main>
      <Footer />
    </Router>
  );
}

export default App;