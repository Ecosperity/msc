let jobModal = document.getElementById('btnjobPreview');
    let divcontentPreview = document.getElementById('divcontentPreview');
    let job_title = document.getElementById('id_job_title');
    let role = document.getElementById('id_role'); 
    let functional_area = document.getElementById('id_functional_area');    
    let industry = document.getElementById('id_industry');    
    let no_of_openings = document.getElementById('id_no_of_openings');    
    let country = document.getElementById('id_country');    
    let place = document.getElementById('id_place');  
    let experience = document.getElementById('id_experience');    
        
    jobModal.addEventListener('click', function () {
    let job_description = tinyMCE.get('id_job_description').getContent();    
    let salary = document.getElementById('id_salary').value;
    
    let publish = document.getElementById('id_publish').checked;
    if(publish==true){ publish = "YES";}else{ publish="NO";}
    let skillset = document.getElementsByName('skills'); 
    
    divcontentPreview.innerHTML="<b>Job title :</b> "+job_title.value;
    divcontentPreview.innerHTML+="<hr>";
    divcontentPreview.innerHTML+="<b>Role :</b> " +role.value;
    divcontentPreview.innerHTML+="<hr>";
    divcontentPreview.innerHTML+="<b>Job description : </b><br/>"+job_description;
    divcontentPreview.innerHTML+="<hr>";    
    divcontentPreview.innerHTML+=`<b>Experience :</b>  ${ experience.value}`;
    divcontentPreview.innerHTML+="<hr>";
    divcontentPreview.innerHTML+="<b>Functional area :</b> "+ functional_area.value;
    divcontentPreview.innerHTML+="<hr>";
    divcontentPreview.innerHTML+="<b>Industry :</b> "+ industry.value;
    divcontentPreview.innerHTML+="<hr>";
    divcontentPreview.innerHTML+="<b>No of openings :</b> "+ no_of_openings.value;
    divcontentPreview.innerHTML+="<hr>";
    divcontentPreview.innerHTML+="<b>Salary :</b> "+ salary;
    divcontentPreview.innerHTML+="<hr>";
    divcontentPreview.innerHTML+="<b>Country :</b> "+ country.value;
    divcontentPreview.innerHTML+="<hr>";
    divcontentPreview.innerHTML+="<b>Place :</b> "+ place.value;
    divcontentPreview.innerHTML+="<hr>";
    divcontentPreview.innerHTML+="<b>Publish :</b> "+ publish;
    divcontentPreview.innerHTML+="<hr>";
    divcontentPreview.innerHTML+="<b>Skillset:</b> "    
    for (var i=0; i < skillset.length; i++) {
        divcontentPreview.innerHTML+= `<span class="badge bg-success mx-1">${skillset[i].value}</span>`;       
    }
    
    })