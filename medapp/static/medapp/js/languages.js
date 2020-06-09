var dataReload = document.querySelectorAll('[data-reload]');

//language translations

let language = {
	eng: {
		welcome: 'Find the right professional for your needs',
		getstarted: 'Get stared',
		servicedesc: 'Service',
		ourconsult: 'Our Consultants'
	},
	bg: {
		welcome: 'Намери правилния лекар за своите нужди',
		getstarted: 'Влез',
		servicetext: 'Услуга',
		servicetext2: 'Услуга2',
		servicetext3: 'Услуга3',
		servicetext4: 'Услуга4',
		servicetext5: 'Услуга5',
		servicetext6: 'Услуга6',
		ask: 'Задайте ни въпрос',
		btnsend: 'Изпрати',
		ourconsult: 'Нашите консултанти',
		articlenew: 'Последни статии',
		author1: 'Автор1',
		author2: 'Автор2',
		author3: 'Автор3',
		art1: 'Статия 1',
		art2: 'Статия 2',
		art3: 'Статия 3',
		homebtn: 'начало',
		blogbtn: 'блог',
		servicebtn: 'услуги',
		consultantbtn: 'консултанти',
		textusbtn: 'пишете ни'
	}
};

if (window.location.hash) {
	if (window.location.hash === '#bg') {
		hi.textContent = language.bg.welcome;
		getstarted.textContent = language.bg.getstarted;
		servicetext.textContent = language.bg.servicetext;
		servicetext2.textContent = language.bg.servicetext2;
		servicetext3.textContent = language.bg.servicetext3;
		servicetext4.textContent = language.bg.servicetext4;
		servicetext5.textContent = language.bg.servicetext5;
		servicetext6.textContent = language.bg.servicetext6;
		ourconsult.textContent = language.bg.ourconsult;
		ask.textContent = language.bg.ask;
		articlenew.textContent = language.bg.articlenew;
		author1.textContent = language.bg.author1;
		author2.textContent = language.bg.author2;
		author3.textContent = language.bg.author3;
		art1.textContent = language.bg.art1;
		art2.textContent = language.bg.art2;
		art3.textContent = language.bg.art3;
		btnsend.textContent = language.bg.btnsend;
		homebtn.textContent = language.bg.homebtn;
		blogbtn.textContent = language.bg.blogbtn;
		servicebtn.textContent = language.bg.servicebtn;
		textusbtn.textContent = language.bg.textusbtn;
		consultantbtn.textContent = language.bg.consultantbtn;

		document.getElementById('askname').placeholder = 'Име';
		document.getElementById('askemail').placeholder = 'E-mail';
		document.getElementById('asktopic').placeholder = 'Тема';
		document.getElementById('askmessage').placeholder = 'Съобщение..';
	}
}

// define onclick illiteration

function timeFunction() {
	setTimeout(function() {
		history.go(0);
	}, 100);
}
