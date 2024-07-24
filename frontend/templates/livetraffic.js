document.addEventListener("DOMContentLoaded", function() {
    const lights = ["red", "yellow", "green"];
    let currentLight = 0;

    setInterval(() => {
        lights.forEach((light, index) => {
            document.getElementById(light).style.opacity = index === currentLight ? 1 : 0.3;
        });
        currentLight = (currentLight + 1) % lights.length;
    }, 2000);
});