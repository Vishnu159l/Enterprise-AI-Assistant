import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';

function Login(){
    const navigate = useNavigate();
    async function handleLogin(e){
        e.preventDefault();
        const empid = document.getElementById("empidInput").value;
        const password = document.getElementById("passwordInput").value;
        if (!empid || !password) {
            document.getElementById('ps').innerHTML = "Invalid Credentials.";
            return;
        }
        try{
            const response = await fetch('http://127.0.0.1:8000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    emp_id: empid,
                    password: password
                }),
            });
            const result = await response.json();
                
            if(!result.token_type){
                document.getElementById('ps').innerHTML = result.detail;
                return;
            }
            console.log(result);
            localStorage.setItem('token', result.access_token);
            localStorage.setItem('userName', result.username);
            navigate('/Dashboard');
        }
        catch(error){
            console.log("brr");
        }
    }
    return(
        <div className="login-body">
            <div className="login-div">
                <p id="loginTitle">Log In</p>
                <form onSubmit={handleLogin}>
                    <div>
                        <input className="username" type="text" placeholder="Emp ID" id="empidInput"/>
                        <span id="p"></span>
                        <input className="password" type="password" placeholder="Password" id="passwordInput"/>
                        <span id="ps"></span>
                    </div>
                    <div>
                        <br/>
                        <button className="submit-button" type="submit">Log In</button>
                    </div>
                </form>
            </div>
        </div>
    )
}

export default Login;