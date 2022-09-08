jQuery('#job_form').validate({
	rules:{
		job_title:"required",
		job_description:"required",
        skills:"required",
        no_of_openings:{
            required: true,
            maxlength:4
        }
	},messages:{
		job_title:"Please enter job title",
		job_description:"Please enter job description",
		skills:"Please enter the skils",
		no_of_openings:{
            required: "Please enter the number of openings",
            maxlength: "please enter less than or equal to 5000 nos"
        }
	},
});
