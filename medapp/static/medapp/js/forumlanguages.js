var dataReload = document.querySelectorAll('[data-reload]');

let language = {
	bg: {
		//top bar
		last: 'последна',
		home: 'Начало',
		about: 'За нас',
		profile: 'Профил',
		newpost: 'Нов пост',
		logout: 'Изход',

		//sidebar
		website: 'Уеб сайт',
		sidebars: 'Навигация',
		announcements: 'Обявления',

		login: 'Вход',
		register: 'Регистрация'
	}
};

if (window.location.hash) {
	if (window.location.hash === '#bg') {
		//top bar
		last.textContent = language.bg.last;
		home.textContent = language.bg.home;
		about.textContent = language.bg.about;
		profile.textContent = language.bg.profile;
		newpost.textContent = language.bg.newpost;
		logout.textContent = language.bg.logout;
		updatepost.textContent = language.bg.updatepost;

		//sidebar
		website.textContent = language.bg.website;
		sidebars.textContent = language.bg.sidebars;
		announcements.textContent = language.bg.announcements;

		login.textContent = language.bg.login;
		register.textContent = language.bg.register;
	}
}

function forumTimeFunction() {
	setTimeout(function() {
		history.go(0);
	}, 100);
}
