var firebaseConfig = {
	apiKey: 'AIzaSyCLwGQlTdqalI28W-M_VGknWR7E6-PSkpg',
	authDomain: 'medichelpproject.firebaseapp.com',
	databaseURL: 'https://medichelpproject.firebaseio.com',
	projectId: 'medichelpproject',
	storageBucket: 'medichelpproject.appspot.com',
	messagingSenderId: '579257063454',
	appId: '1:579257063454:web:09d71b134f26a11e03360f',
	measurementId: 'G-NN8R2P9FTR'
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

const auth = firebase.auth();

function signUp() {
	var email = document.getElementById('modalLRInput12');
	var password = document.getElementById('modalLRInput13');
	var repeat = document.getElementById('modalLRInput14');

	if (password.value === repeat.value && password.value.length > 5) {
		const promise = auth.createUserWithEmailAndPassword(email.value, password.value);
		promise.catch((e) => alert(e.message));

		alert('Signed Up');
	} else {
		alert('Password must be matching and longer than 6 characters');
	}
}

function signIn() {
	var email = document.getElementById('modalLRInput10');
	var password = document.getElementById('modalLRInput11');

	const promise = auth.signInWithEmailAndPassword(email.value, password.value);
	// Handle Errors here.
	promise.catch((e) => alert(e.message));
}
/*
firebase.auth().onAuthStateChanged(function(user) {
	if (user) {
		window.location = 'login.html';
	} else {
		console.log('Wrong credentials');
	}
});
*/

function signOut() {
	auth.signOut();
	alert('signed out1');
}
