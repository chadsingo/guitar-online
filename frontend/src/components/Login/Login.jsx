import { useState } from "react";
import styles from "./login.module.css";
import { login } from "./login";


export default function Login(){

    const [username, setUsername] = useState('');
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
                <h2>Login</h2>
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
                    Login
                </button>

                <button type = 'submit'>
                    Create Account
                </button>

                <p>
                    {message}
                </p>

            </form>
        </div>

    );
}


