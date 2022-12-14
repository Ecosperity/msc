let mic = document.getElementById("btn-mic");
let micStop = document.getElementById("btn-mic-stop");
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.continuous = true;
mic.addEventListener("click",function(){
    recognition.start();
    mic.style.background= '#eed484';
    mic.style.borderRadius = '50%';
    // mic.classList.add("blink_me")   
    // Speak("I am listening you")
})

micStop.addEventListener("click",function(){   
    recognition.stop();
    // mic.style.background= '#bc32ef';
    // mic.style.borderRadius= '60%';    
})

recognition.onend = function(){
mic.style.background = '';
}

recognition.onresult = function(event) {
    let resultIndex = event.resultIndex;
    let transcript = event.results[resultIndex][0].transcript
    ChattingData(transcript);
}