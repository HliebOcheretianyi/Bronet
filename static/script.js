let currentIndex = 0;
const totalProfiles = document.querySelectorAll('.profile-card').length;
const profileWrapper = document.querySelector('.profile-wrapper');

function showNextProfile() {
    if (currentIndex < totalProfiles - 1) {
        currentIndex++;
        updateProfilePosition();
    }
}

function showPreviousProfile() {
    if (currentIndex > 0) {
        currentIndex--;
        updateProfilePosition();
    }
}

function updateProfilePosition() {
    // Smoothly transition the profile-wrapper to the next card by translating it horizontally
    profileWrapper.style.transform = `translateX(-${currentIndex * 100}%)`;
}

function showNextProfile() {
    if (currentIndex < totalProfiles - 1) {
        currentIndex++;
    } else {
        currentIndex = 0; // Loop back to the first profile
    }
    updateProfilePosition();
}

function showPreviousProfile() {
    if (currentIndex > 0) {
        currentIndex--;
    } else {
        currentIndex = totalProfiles - 1; // Loop back to the last profile
    }
    updateProfilePosition();
}