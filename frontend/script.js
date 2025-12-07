console.log("script.js loaded");

document.getElementById("analyzeBtn").addEventListener("click", async () => {
    console.log("Analyze button clicked");

    const file = document.getElementById("fileInput").files[0];
    if (!file) {
        alert("Please select a file.");
        return;
    }

    document.getElementById("loading").style.display = "block";

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("http://127.0.0.1:8000/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        // Clean summary text (remove markdown)
        const cleanText = text =>
            text
                .replace(/\*\*(.*?)\*\*/g, "$1")   // remove **bold**
                .replace(/\*(.*?)\*/g, "$1")       // remove *italic*
                .replace(/\\n/g, "\n")             // convert \n to real newlines
                .replace(/\n+/g, "\n")             // remove extra line breaks
                .trim();

        document.getElementById("qualityReport").textContent =
            cleanText(data.quality_report || "No report available.");

        document.getElementById("summary").textContent =
            cleanText(data.summary || "No summary available.");

    } catch (err) {
        document.getElementById("qualityReport").textContent = "Error analyzing file.";
        document.getElementById("summary").textContent = "";
    }

    document.getElementById("loading").style.display = "none";
});
