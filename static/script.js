document.addEventListener('DOMContentLoaded', init);

// initialize the app
function init(e) {
	const inputFile = document.getElementById('dog-picture');
	const form = document.getElementById('post-img');
	inputFile.addEventListener('change', displayImg);
	form.addEventListener('submit', postImg);
}

function displayImg(e) {
	const messagesPlace = document.getElementById('result-page');

	const file = e.target.files[0];
	if (file) {
		if (file.type !== 'image/jpeg' && file.type !== 'image/png') {
			messagesPlace.innerHTML = `<p class="alert alert-danger" role="alert">
				Le format du fichier est incorrecte.
			</p>`;
			return;
		}
		// Clear messages
		messagesPlace.innerHTML = '';

		const imgPlace = document.getElementById('img-place');
		imgPlace.innerHTML = `<img
            src="${URL.createObjectURL(file)}"
            alt="L'image que vous avez téléchargée"
            class="render-image img-fluid mt-3"
        />`;
	}
}

function manageResult(res) {
	const messagesPlace = document.getElementById('result-page');
	const { breed, error } = res;
	if (error) {
		messagesPlace.innerHTML = `<p class="alert alert-danger" role="alert">${error}</p>`;
	} else if (breed) {
		messagesPlace.innerHTML = `<p class="alert alert-success" role="alert">
			Ce chien est un ${breed}
		</p>`;
	} else {
		messagesPlace.innerHTML = `<p class="alert alert-secondary" role="alert">Aucun resultat.</p>`;
	}

	// Stop loader
	actionIcon = document.getElementById('action-icon');
	loader = document.getElementById('loader');
	actionIcon.classList.remove('d-none');
	loader.classList.add('d-none');
}

function clearMessages() {}

function postImg(e) {
	e.preventDefault();
	e.stopPropagation();
	const formData = new FormData(e.target);
	post('/', formData, manageResult);

	// Clear messages
	const messagesPlace = document.getElementById('result-page');
	messagesPlace.innerHTML = '';

	// Start loader
	actionIcon = document.getElementById('action-icon');
	loader = document.getElementById('loader');
	actionIcon.classList.add('d-none');
	loader.classList.remove('d-none');
}

function post(url, body, callback) {
	fetch(url, {
		method: 'POST',
		body,
	})
		.then(res => res.json())
		.then(callback)
		.catch(error => {
			if (error.message) error = error.message;
			console.error(error);
			callback({ error });
		});
}
