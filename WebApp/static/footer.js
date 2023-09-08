function updateDateTime() {
    const currentDate = new Date();
    const options = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
        //   timeZoneName: 'short'
    };
    const formattedDate = currentDate.toLocaleString('en-US', options);
    document.getElementById('current-year').textContent = formattedDate;
}
updateDateTime();
setInterval(updateDateTime);
