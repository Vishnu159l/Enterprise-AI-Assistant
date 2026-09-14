import React from 'react';
import profile from './profile-svgrepo-com.svg'
import './Dashboard.css';

function Dashboard(){
    const emp = localStorage.getItem("userName");
    function toggleDropdown(){
        const dropdown = document.getElementById('dropdown');
        dropdown.classList.toggle('active');
    }

    function logout(){
        localStorage.clear();
    }

    async function rag_request(){
        const ragResponse = document.getElementById('p2');
        const ragQuery = document.getElementById('p1').value;
        console.log(ragQuery)
        ragResponse.style.display = "block"; 
        ragResponse.innerText = "Thinking...."
        const token = localStorage.getItem("token")
        console.log(token)
        try {
            const res = await fetch('http://127.0.0.1:8000/user/query', {
                method: 'POST',
                headers: {
                    'accept': 'application/json',
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ user_input: ragQuery }),
            });
            const result = await res.json();
            console.log(result)
            ragResponse.innerHTML = result.rag_response;
        }
        catch (error) {
            console.error("Query Error:", error);
        }
    }
    return(
        <div>
            <div className='nav-container'>
                <div className='Logo'>
                    <p>Logo</p>
                </div>
                <div className='Profile'>
                    <button className="profile-button" onClick={toggleDropdown}>
                        <img src={profile} alt="Profile"/>
                    </button>
                    <div className="dropdown-menu" id="dropdown">
                        <p>{emp}</p>
                        <a href="/" onClick={logout}>Logout</a>
                    </div>
                </div>
            </div>
            <div className='user-container'>
                <textarea className="query-input" placeholder='Enter Query' id='p1'></textarea>
                <button className='query-button' onClick={rag_request}>Submit</button>
            </div>
            <div className='response-container'>
                <p>
                    RAG response:
                </p>
                <p className='resp' id='p2'>

                </p>
            </div>
        </div>
    )
}

export default Dashboard;