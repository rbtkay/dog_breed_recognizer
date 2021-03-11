document.addEventListener('DOMContentLoaded', init);

// initialize the app
function init(e) {
	const inputFile = document.getElementById('dog_picture');
	inputFile.addEventListener('change', displayImg);
}

function displayImg(e) {
	const { files } = e.target;
	if (files.length > 0) {
		console.error("Vous essayez d'uploder plus d'une image");
		return;
	}
	if (files[0]) {
		if (file.type !== 'image/jpeg' && file.type !== 'image/png') {
			console.error('Le format du fichier est incorrecte.');
			return;
		}
		const place = document.getElementById('img-place');
		place.innerHTML = `<img
            src="${URL.createObjectURL(files[0])}"
            alt="L'image que vous avez téléchargée"
            className="render-image"
        />`;
	}
}
