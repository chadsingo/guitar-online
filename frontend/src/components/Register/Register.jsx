import { useState } from "react";
import styles from "./register.module.css";
import { register } from "./register";


export default function Register(){

    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('')


    async function handleSubmit(e){
        e.preventDefault();

        const result = await login(username, password);

        if (result.success){
            setMessage("Login Successful!");
        }
        else{
            setMessage(result.message);
        }
    }


    return (
        <div className = {styles.container}>
            <form onSubmit = {handleSubmit} className = {styles.form}>
                <h2>Create An Account</h2>
                <input 
                    type = 'email'
                    placeholder = 'Email'
                    value = {password}
                    onChange = {(e) => setPassword(e.target.value)}
                />
                <input
                    type = 'text'
                    placeholder = 'Username'
                    value = {username}
                    onChange = {(e) => setUsername(e.target.value)}
                />
                <input 
                    type = 'password'
                    placeholder = 'Password'
                    value = {password}
                    onChange = {(e) => setPassword(e.target.value)}
                />

                <button type = 'submit'>
                    Register
                </button>

                <p>
                    {message}
                </p>

            </form>
        </div>

    );
}


