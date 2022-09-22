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


  $('.end-chat').click(function () {
    $('.chat-body').addClass('hide');
    $('.chat-input').addClass('hide');
    $('.chat-session-end').removeClass('hide');
    $('.chat-header-option').addClass('hide');
  });
  $('#btnChatClose').click(function () {
    $(".chat-bot-icon").children('svg').toggleClass('animate');
    $('.chat-screen').toggleClass('show-chat');
  });

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
  $('.chat-body').append('<div class="chat-bubble me">' + text + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
  $('.chat-body').append(`<div class="divTyping chat-bubble you" id="divTyping"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="margin: auto;display: block;shape-rendering: auto;width: 43px;height: 20px;" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid">
                <circle cx="0" cy="44.1678" r="15" fill="#ffffff">
                    <animate attributeName="cy" calcMode="spline" keySplines="0 0.5 0.5 1;0.5 0 1 0.5;0.5 0.5 0.5 0.5" repeatCount="indefinite" values="57.5;42.5;57.5;57.5" keyTimes="0;0.3;0.6;1" dur="1s" begin="-0.6s"></animate>
                </circle> <circle cx="45" cy="43.0965" r="15" fill="#ffffff">
                <animate attributeName="cy" calcMode="spline" keySplines="0 0.5 0.5 1;0.5 0 1 0.5;0.5 0.5 0.5 0.5" repeatCount="indefinite" values="57.5;42.5;57.5;57.5" keyTimes="0;0.3;0.6;1" dur="1s" begin="-0.39999999999999997s"></animate>
            </circle> <circle cx="90" cy="52.0442" r="15" fill="#ffffff">
                <animate attributeName="cy" calcMode="spline" keySplines="0 0.5 0.5 1;0.5 0 1 0.5;0.5 0.5 0.5 0.5" repeatCount="indefinite" values="57.5;42.5;57.5;57.5" keyTimes="0;0.3;0.6;1" dur="1s" begin="-0.19999999999999998s"></animate>
            </circle></svg></div>`);
  $('#txtmessage').val('');
  $('#txtmessage').attr('disabled', 'disabled');
  var csrftoken = $("[name=csrfmiddlewaretoken]").val();
  URL = 'chatbot/BotConversation';
  $.ajax({
    url: URL,
    type: 'POST',
    headers: { "X-CSRFToken": csrftoken },
    data: {
      'text': text
    }
  }).done(function (data) {    
    if(data.title=='jobs'){       
      // window.open("jobssearch/");
      $('.chat-body').append('<div class="chat-bubble you">' + data.q + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
      $('.chat-body').append(`<div class="form-group border border-2 text-center">                    
      <input type="button" id="btnJobsIndia" onclick="location_btn_event('india')" value="I am looking for jobs in India" class="btn btn-sm btn-outline-success my-1">
      <input type="button" id="btnJobsItaly" onclick="location_btn_event('italy')" value="I am looking for jobs in Italy" class="btn btn-sm btn-outline-success my-1">
      <input type="button" id="btnJobsUSA" onclick="location_btn_event('usa')" value="I am looking for jobs in USA" class="btn btn-sm btn-outline-success my-1">
      <input type="button" id="btnJobsSwitzerland" onclick="location_btn_event('switzerland')" value="I am looking for jobs in Switzerland" class="btn btn-sm btn-outline-success my-1">
      </div>`).animate({scrollTop: $('.chat-body').prop("scrollHeight")}, 400); 
    }else if(data.title=='msc'){       
      window.open("chatbot/msc-technology/");
      $('.chat-body').append('<div class="chat-bubble you">' + data.q + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
    }else if(data.title=='location'){       
      // window.open("msc-technology/");
      $('.chat-body').append('<div class="chat-bubble you">' + data.q + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
     
    }
    else if(data.location !=undefined){   
      window.open("chatbot/jobssearch/?skill=" + data.skill +"&title="+data.title +"&location="+data.location);
      $('.chat-body').append('<div class="chat-bubble you">' + data.q + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
    }else if(data.page !=undefined){      
      window.open("chatbot/jobssearch/?skill=" + data.skill +"&title="+data.title);
      $('.chat-body').append('<div class="chat-bubble you">' + data.q + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
    }else{
      $('.chat-body').append('<div class="chat-bubble you">' + data + '</div>').animate({ scrollTop: $('.chat-body').prop("scrollHeight") }, 400);
      $('.chat-body').append(`<div class="form-group border border-2 text-center">                    
      <input type="button" id="btnmscTechnology" onclick="menubar_btn_event('mscTechnology')" value="I want know about MSC Technology" class="btn btn-sm btn-outline-secondary my-1">
      <input type="button" id="btnJobs" onclick="menubar_btn_event('jobs')" value="I am looking for job" class="btn btn-sm btn-outline-success my-1">
                </div>`).animate({scrollTop: $('.chat-body').prop("scrollHeight")}, 400);
    }
    $('#txtmessage').removeAttr('disabled');
    $('#txtmessage').focus();
    $(".divTyping").remove();
    Speak("I am listening you")
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
            </circle></svg> I am listening you</div>`);

  var csrftoken = $("[name=csrfmiddlewaretoken]").val();
  URL = 'chatbot/speaking';
  $.ajax({
    url: URL,
    type: 'POST',
    headers: { "X-CSRFToken": csrftoken },
    data: {
      'text': text
    }
  }).done(function (data) {
    recognition.start();
    mic.style.background = '#bc32ef';
    mic.style.borderRadius = '60%';
    setTimeout(() => {
      $(".divTyping").remove();
    }, 4000);
  });
}

function location_btn_event(val){
  // alert(val);
  let cdata = `location ${val}`;
  ChattingData(cdata);
}
function menubar_btn_event(val){
  if(val=='mscTechnology'){     
      ChattingData("More About MSC Technology");     
      $('#btnmscTechnology').removeClass("btn-outline-secondary").addClass("btn-success").attr('disabled',true);;
      $('#btnJobs').attr('disabled',true);   
      }
  if(val=='jobs'){  
    ChattingData("I am looking for jobs");    
      $('#btnJobs').removeClass("btn-outline-success").addClass("btn-success").attr('disabled',true);;
      $('#btnmscTechnology').attr('disabled',true);  
      
  }
}