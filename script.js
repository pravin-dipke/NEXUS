const container = document.getElementById('container');
const loginButton = document.getElementById('login');
const registerButton = document.getElementById('register');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const nameInput = document.getElementById('nameInput');
const usernameSignUpInput = document.getElementById('usernameInput');
const passwordSignUpInput = document.getElementById('passwordInput');

const database = {
    users: [
        { username: 'pravin', password: '123', name: 'Pravin' }
    ]
};

loginButton.addEventListener('click', () => {
    container.classList.remove('active');
});

registerButton.addEventListener('click', () => {
    container.classList.add('active');
});

function handleSignUp(event) {
    event.preventDefault();
    const name = nameInput.value;
    const username = usernameSignUpInput.value;
    const password = passwordSignUpInput.value;

    const existingUser = database.users.find(user => user.username === username);
    if (existingUser) {
        alert('Username already exists. Please choose a different username.');
        return;
    }

    database.users.push({ username, password, name });
    alert('Sign up successful!');
    nameInput.value = '';
    usernameSignUpInput.value = '';
    passwordSignUpInput.value = '';
}

function handleSignIn(event) {
    event.preventDefault();
    const username = usernameInput.value;
    const password = passwordInput.value;

    const user = database.users.find(user => user.username === username && user.password === password);
    if (user) {
        window.location.href = 'http://127.0.0.1:7860';
    } else {
        alert('Invalid username or password');
    }
}