document.addEventListener("DOMContentLoaded", () => {
    // Get the cards by their IDs
    const clothesCard = document.getElementById('clothes-card');
    const accessoriesCard = document.getElementById('accessories-card');
    const personalItemsCard = document.getElementById('personal-items-card');

    // Add event listeners to the cards
    clothesCard.addEventListener('click', () => {
        window.location.href = '/clothes';  // Navigate to clothes page
    });

    accessoriesCard.addEventListener('click', () => {
        window.location.href = '/accessories';  // Navigate to accessories page
    });

    personalItemsCard.addEventListener('click', () => {
        window.location.href = '/personal_items';  // Navigate to personal items page
    });
});