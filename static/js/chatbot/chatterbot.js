$(document).ready(function () {
  let d = new Date();
  let weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
  let day = weekday[d.getDay()]
  let time = d.toLocaleTimeString('en-US').toLowerCase().replace(/([\d]+:[\d]+):[\d]+(\s\w+)/g, "$1$2");
  $('.chat-start').html(day + ", " + time);

  setTimeout(() => {
    $('.chat-bot-icon').children('svg').toggleClass('animate');
    $('.chat-screen').toggleClass('show-chat');
    ChattingData('');
  }, 3000);

  //Toggle fullscreen
  $(".chat-bot-icon").click(function (e) {
    $(this).children('svg').toggleClass('animate');
    $('.chat-screen').toggleClass('show-chat');
  })

  $('#txtmessage').keyup(function (event) {
    if (event.keyCode === 13) {
      var msg = $('#txtmessage').val();
      if (msg == '') {
        $('#txtmessage').focus();
      } else {
        ChattingData(msg);
      }
    }
  });
  $("#linkSendText").click(function () {
    var msg = $('#txtmessage').val();
    if (msg == '') {
      $('#txtmessage').focus();
    } else {
      ChattingData(msg);
    }
  });

});


function ChattingData(text) {
  recognition.stop();
  if(text !==''){
    $('.chat-body').append('<div class="chat-bubble mt-1 me">' + text + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
  }
  $('.chat-body').append(`<div class="divTyping chat-bubble you" id="divTyping"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto;display: block;shape-rendering: auto;width: 43px;height: 20px;" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
                <circle cx="0" cy="44.1678" r="15" fill="#000000">
                    <animate attributeName="cy" calcMode="spline" keySplines="0 0.5 0.5 1;0.5 0 1 0.5;0.5 0.5 0.5 0.5" repeatCount="indefinite" values="57.5;42.5;57.5;57.5" keyTimes="0;0.3;0.6;1" dur="1s" begin="-0.6s"></animate>
                </circle> <circle cx="45" cy="43.0965" r="15" fill="#000000">
                <animate attributeName="cy" calcMode="spline" keySplines="0 0.5 0.5 1;0.5 0 1 0.5;0.5 0.5 0.5 0.5" repeatCount="indefinite" values="57.5;42.5;57.5;57.5" keyTimes="0;0.3;0.6;1" dur="1s" begin="-0.39999999999999997s"></animate>
            </circle> <circle cx="90" cy="52.0442" r="15" fill="#000000">
                <animate attributeName="cy" calcMode="spline" keySplines="0 0.5 0.5 1;0.5 0 1 0.5;0.5 0.5 0.5 0.5" repeatCount="indefinite" values="57.5;42.5;57.5;57.5" keyTimes="0;0.3;0.6;1" dur="1s" begin="-0.19999999999999998s"></animate>
            </circle></svg></div>`);
  $('#txtmessage').val('');
  $('#txtmessage').attr('disabled', 'disabled');
  var csrftoken = $("[name=csrfmiddlewaretoken]").val();
  URL = '/chatbot/BotConversation/';
  $.ajax({
    url: URL,
    type: 'GET',
    // headers: { "X-CSRFToken": csrftoken },
    data: {
      'text': text
    }
  }).done(function (data) { 
    recognition.stop();
    if(data.title=='jobs'){       
      // window.open("jobssearch/");
      $('.chat-body').append('<div class="chat-bubble you">' + data.q + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
      $('.chat-body').append(`<div class="form-group border border-2 text-center">                    
      <input type="button" id="btnJobsIndia" onclick="location_btn_event('india')" value="I am looking for jobs in India" class="btn btn-sm btn-outline-success rounded-pill my-1">
      <input type="button" id="btnJobsItaly" onclick="location_btn_event('italy')" value="I am looking for jobs in Italy" class="btn btn-sm btn-outline-warning rounded-pill my-1">
      <input type="button" id="btnJobsUSA" onclick="location_btn_event('usa')" value="I am looking for jobs in USA" class="btn btn-sm btn-outline-info rounded-pill my-1">
      <input type="button" id="btnJobsSwitzerland" onclick="location_btn_event('switzerland')" value="I am looking for jobs in Switzerland" class="btn btn-sm btn-outline-danger rounded-pill my-1">
      </div>`).animate({scrollTop: $('.chat-body').prop("scrollHeight")}, 400); 
    }else if(data.title=='msc technology'){       
      window.open("/chatbot/msc-technology/");
      $('.chat-body').append('<div class="chat-bubble you">' + data.q + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
    }else if(data.title=='location'){       
      window.open("msc-technology/"); 
       $('.chat-body').append('<div class="chat-bubble you">' + data.q + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
      data.skill_list.forEach(element => {$('.chat-body').append(`<input type="button" value='${element}' onclick="skills_btn_event('${element}')" class="btn btn-sm btn-outline-secondary my-1 rounded-pill"></input>`) })
      $('.chat-body').append('<div class="chat-bubble you">Select your Skill</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
    }
    else if(data.location !=undefined){   
      window.open("/chatbot/jobssearch/?skill=" + data.skill +"&title="+data.title +"&location="+data.location);
      $('.chat-body').append('<div class="chat-bubble you">' + data.q + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
    }else if(data.page !=undefined){      
      window.open("/chatbot/jobssearch/?skill=" + data.skill +"&title="+data.title);
      $('.chat-body').append('<div class="chat-bubble you">' + data.q + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
    }else if(data.title =='thankYou'){ 
      recognition.stop();
      $('.chat-body').append('<div class="chat-bubble you">' + data.q + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
    }else{
      $('.chat-body').append('<div class="chat-bubble you">' + data + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
      $('.chat-body').append(`<div class="form-group border border-2 text-center">                    
      <input type="button" id="btnmscTechnology" onclick="menubar_btn_event('mscTechnology')" value="I would like to know about MSC Technology." class="btn btn-sm btn-outline-secondary my-1 rounded-pill text-wrap">
      <input type="button" id="btnmscTechnologyIndia" onclick="menubar_btn_event('mscTechnologyIndia')" value="I would like to know news about MSC Technology India." class="btn btn-sm btn-outline-warning my-1 rounded-pill text-wrap">
      <input type="button" id="btnmscTechnologyManagement" onclick="menubar_btn_event('mscTechnologyManagement')" value="I would like know more about the management." class="btn btn-sm btn-outline-info my-1 rounded-pill text-wrap">
      <input type="button" id="btnJobs" onclick="menubar_btn_event('jobs')" value="I am looking for jobs." class="btn btn-sm btn-outline-success my-1 rounded-pill">
                </div>`).animate({scrollTop: $('.chat-body').prop("scrollHeight")}, 400);
    }
    $('#txtmessage').removeAttr('disabled');
    $('#txtmessage').focus();
    $(".divTyping").remove();
    Speak("I am listening you")
    recognition.start();
    mic.style.background= '#eed484';
    mic.style.borderRadius= '50%';
  });
}

function Speak(text) {
  $('.chat-body').append(`<div class="divTyping chat-bubble you" id="divTyping"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto;display: block;shape-rendering: auto;width: 43px;height: 20px;" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
                <circle cx="0" cy="44.1678" r="15" fill="#ffffff">
                    <animate attributeName="cy" calcMode="spline" keySplines="0 0.5 0.5 1;0.5 0 1 0.5;0.5 0.5 0.5 0.5" repeatCount="indefinite" values="57.5;42.5;57.5;57.5" keyTimes="0;0.3;0.6;1" dur="1s" begin="-0.6s"></animate>
                </circle> <circle cx="45" cy="43.0965" r="15" fill="#ffffff">
                <animate attributeName="cy" calcMode="spline" keySplines="0 0.5 0.5 1;0.5 0 1 0.5;0.5 0.5 0.5 0.5" repeatCount="indefinite" values="57.5;42.5;57.5;57.5" keyTimes="0;0.3;0.6;1" dur="1s" begin="-0.39999999999999997s"></animate>
            </circle> <circle cx="90" cy="52.0442" r="15" fill="#ffffff">
                <animate attributeName="cy" calcMode="spline" keySplines="0 0.5 0.5 1;0.5 0 1 0.5;0.5 0.5 0.5 0.5" repeatCount="indefinite" values="57.5;42.5;57.5;57.5" keyTimes="0;0.3;0.6;1" dur="1s" begin="-0.19999999999999998s"></animate>
            </circle></svg></div>`);

    recognition.start();
    mic.style.background= '#eed484';
    mic.style.borderRadius= '50%';
}

function location_btn_event(val){
  let cdata = `${val}`;
  ChattingData(cdata);
}

function skills_btn_event(val){ 
  let skilldata = `${val}`;  
   $('#txtmessage').val($('#txtmessage').val() +" "+ skilldata);
}

function menubar_btn_event(val){
  if(val=='mscTechnology'){     
      ChattingData("I would like to know about MSC Technology.");     
      $('#btnmscTechnology').removeClass("btn-outline-secondary").addClass("btn-success").attr('disabled',true);;
      $('#btnJobs').attr('disabled',true);   
      $('#btnmscTechnologyIndia').attr('disabled',true);   
      $('#btnmscTechnologyManagement').attr('disabled',true);   
      }
  if(val=='mscTechnologyIndia'){     
      ChattingData("I would like to know news about MSC Technology India.");     
      $('#btnmscTechnologyIndia').removeClass("btn-outline-info").addClass("btn-info").attr('disabled',true);
      $('#btnJobs').attr('disabled',true);   
      $('#btnmscTechnology').attr('disabled',true);   
      $('#btnmscTechnologyManagement').attr('disabled',true); 
      }
  if(val=='mscTechnologyManagement'){     
      ChattingData("I would like know more about the management.");     
      $('#btnmscTechnologyManagement').removeClass("btn-outline-info").addClass("btn-info").attr('disabled',true);
      $('#btnJobs').attr('disabled',true);   
      $('#btnmscTechnology').attr('disabled',true);
      $('#btnmscTechnologyIndia').attr('disabled',true);      
      }
  if(val=='jobs'){  
    $('#btnJobs').removeClass("btn-outline-success").addClass("btn-success").attr('disabled',true);;
    $('#btnmscTechnology').attr('disabled',true);  
    $('#btnmscTechnologyIndia').attr('disabled',true);  
    $('#btnmscTechnologyManagement').attr('disabled',true);  
    ChattingData("I am looking for jobs.");    
      
  }
}

// Dragble JS start
dragElement(document.getElementById("mydiv"));
function dragElement(elmnt) {
  var pos1 = 0, pos2 = 10, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "header")) {
    // if present, the header is where you move the DIV from:
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
  } else {
    // otherwise, move the DIV from anywhere inside the DIV:
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
  }
}
// Dragble JS end