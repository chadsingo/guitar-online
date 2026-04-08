const API_URL = import.meta.env.VITE_API_URL;

export async function register(username, password) {
    const response = await fetch(`${API_URL}/register`, {
        
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: 'include',
        body: JSON.stringify({
            username: username,
            password: password,
            email: email
        })
    });

    const data = await response.json();
    console.log(import.meta.env.VITE_API_URL);

    if (!response.ok) {
        return {success: false, message: data.error};
    }

    return {success: true, message: data.message};

}
