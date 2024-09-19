
    document.addEventListener("DOMContentLoaded", function() {
        const lights = ["red", "yellow", "green"];
        let currentLight = 0;
        let intervals = [3000, 1000, 5000];  // Red for 3 seconds, Yellow for 1 second, Green for 5 seconds

        function changeLight() {
            lights.forEach((light, index) => {
                document.getElementById(light).style.opacity = index === currentLight ? 1 : 0.3;
            });

            // Set the next light change after the current interval
            setTimeout(() => {
                currentLight = (currentLight + 1) % lights.length;
                changeLight();
            }, intervals[currentLight]);
        }

        changeLight();  // Start the light cycle
    });

