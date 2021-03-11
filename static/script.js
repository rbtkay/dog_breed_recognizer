document.addEventListener('DOMContentLoaded', init);

// initialize the app
function init(e) {
	const inputFile = document.getElementById('dog_picture');
	inputFile.addEventListener('change', displayImg);
}

function displayImg(e) {
	const { files } = e.target;
	if (files.length > 1) {
		console.error("Vous essayez d'uploder plus d'une image");
		return;
	}
	const file = files[0];
	if (file) {
		if (file.type !== 'image/jpeg' && file.type !== 'image/png') {
			console.error('Le format du fichier est incorrecte.');
			return;
		}
		const place = document.getElementById('img-place');
		place.innerHTML = `<img
            src="${URL.createObjectURL(file)}"
            alt="L'image que vous avez téléchargée"
            class="render-image img-fluid mt-3"
        />`;
	}
}
