import React from 'react';

export const Form = ({onFormChange, onFormSubmit}) => {


    const handleChange = (event) => {
        onFormChange(event.target.value)
    }
    
    const handleSubmit = (event) => {
        event.preventDefault();
        onFormSubmit()
    }

    return (
        <>
        <p>Enter a sentence</p>
        <form onSubmit={handleSubmit}>
            <textarea type='text' required onChange={handleChange} className="input"></textarea>
            <input type="submit" value="Predict" className='btn'></input>
        </form>
        </>
    );


}