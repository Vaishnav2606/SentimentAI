import { useState } from "react"
import React from 'react'
import { Form } from "./Form"

export const HomePage = () => {

    const [prediction, setPrediction] = useState('')

    const [text, setText] = useState('')

    const formSubmit = () => {
        fetch('/predict',{
            method: 'POST',
            body: JSON.stringify({
                data:text
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        }).then(response=>response.json()).then(message=>{console.log(message);setPrediction(message.data)})
    }

    return(
        <>
        
        <div className="main-body">
            <div className="title-container">
                <h1 className="title">SentimentAI</h1>
                <p className="title-description">
                    This is a smart AI which is capable of predicting the sentiment of a text given to it.
                    It uses the concept of Machine Learning, logistic regression to be more precise, and has been
                    trained on more the 1.5 million twitter tweets. 
                
                </p>
            </div>
            <div className="form-container">
                <Form onFormSubmit={formSubmit} onFormChange={setText}/>
                <h1>Predicted Sentiment: {prediction}</h1>
            </div>
        </div>
        
        </>
    )

}