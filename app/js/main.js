// Voortgangskleur dynamisch toepassen
document.querySelectorAll('.student-profiel').forEach(profile => {
    const progressElement = profile.querySelector('progress');
    const progressValue = parseInt(progressElement.value);

    const statusIndicator = profile.querySelector('.status-indicator');
    
    // Verwijder eerst alle bestaande klassen om conflicten te voorkomen
    statusIndicator.classList.remove('rood', 'geel', 'groen');

    // Voeg de juiste kleurklasse toe op basis van de voortgangswaarde
    if (progressValue < 50) {
        statusIndicator.classList.add('rood');  // Minder dan 50% wordt rood
    } else if (progressValue < 75) {
        statusIndicator.classList.add('geel');  // Tussen 50% en 75% wordt geel
    } else {
        statusIndicator.classList.add('groen'); // 75% of meer wordt groen
    }
});

// Leerjaar selectie filter logica
const leerjaarSelect = document.getElementById('leerjaar-select');
leerjaarSelect.addEventListener('change', function() {
    const geselecteerdLeerjaar = this.value;

    document.querySelectorAll('.student-profiel').forEach(profile => {
        const studentLeerjaar = profile.getAttribute('data-leerjaar');  // Haal leerjaar op uit data-leerjaar
        
        // Controleer of het leerjaar overeenkomt met de selectie (zorg ervoor dat het juiste type wordt vergeleken)
        if (geselecteerdLeerjaar === "all" || studentLeerjaar === geselecteerdLeerjaar) {
            profile.style.display = "flex";  // Toon student als leerjaar overeenkomt
        } else {
            profile.style.display = "none";  // Verberg student als leerjaar niet overeenkomt
        }
    });
});

function logout() {
    localStorage.removeItem("data");
    localStorage.removeItem("role");
    window.location.href = "index.html";
}

document.querySelector('.logout-btn').addEventListener('click', logout);

if (localStorage.getItem("data") != null) {
    const data = (localStorage.getItem("data"));
    console.log(data);
}