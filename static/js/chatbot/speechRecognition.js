let mic = document.getElementById("btn-mic");
let micStop = document.getElementById("btn-mic-stop");
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.continuous = true;

function speak(text, voice, rate, pitch, volume) {
    // create a SpeechSynthesisUtterance to configure the how text to be spoken 
    let speakData = new SpeechSynthesisUtterance();
    speakData.volume = volume; // From 0 to 1
    speakData.rate = rate; // From 0.1 to 10
    speakData.pitch = pitch; // From 0 to 2
    speakData.text = text;
    speakData.lang = 'en';
    speakData.voice = voice;
    
    // pass the SpeechSynthesisUtterance to speechSynthesis.speak to start speaking 
    speechSynthesis.speak(speakData);
  
  }
  
  function getVoices() {
    let voices = speechSynthesis.getVoices();
    if(!voices.length){
      // some time the voice will not be initialized so we can call spaek with empty string
      // this will initialize the voices 
      let utterance = new SpeechSynthesisUtterance("");
      speechSynthesis.speak(utterance);
      voices = speechSynthesis.getVoices();
    }
    return voices;
  }

if ('speechSynthesis' in window) {
    let voices = getVoices();
    let rate = 1, pitch = 2, volume = 1;
    let text = "Spaecking with volume = 1 rate =1 pitch =2 ";
  
    speak(text, voices[5], rate, pitch, volume);
  
    setTimeout(()=>{ // speak after 2 seconds 
      rate = 0.5; pitch = 1.5, volume = 0.5;
      text = "Spaecking with volume = 0.5 rate = 0.5 pitch = 1.5 ";
      speak(text, voices[10], rate, pitch, volume );
    }, 2000);
  }else{
    console.log(' Speech Synthesis Not Supported 😞'); 
  }

mic.addEventListener("click",function(){
    recognition.start();
    mic.style.background= '#eed484';
    mic.style.borderRadius = '50%';

    if ('speechSynthesis' in window) {
        let voices = getVoices();
        let rate = 1, pitch = 2, volume = 1;
        let text = "Spaecking with volume = 1 rate =1 pitch =2 ";
      
        speak(text, voices[5], rate, pitch, volume);
      
        setTimeout(()=>{ // speak after 2 seconds 
          rate = 0.5; pitch = 1.5, volume = 0.5;
          text = "Spaecking with volume = 0.5 rate = 0.5 pitch = 1.5 ";
          speak(text, voices[10], rate, pitch, volume );
        }, 2000);
      }else{
        console.log(' Speech Synthesis Not Supported 😞'); 
      }
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