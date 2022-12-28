import logo from './logo.svg';
import React, {useState, useEffect} from 'react'; 
import './App.css';
import { HomePage } from './components/HomePage';

// const test = ()=>{
//   fetch('/').then(response=>{
//     if(response.ok){
//       return response.json();
//     }
//   })
// }

function App() {

  return (
  
    <HomePage />
    
  );
}

export default App;
