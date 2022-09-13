jQuery('#job_form').validate({
	rules:{
		job_title:{
			required:true,
			maxlength:100
		},
		job_description:"required",
        skills:{
			required:true,
			maxlength:100
		},
        experience:{
            required: true,
            maxlength:100
        },
		role:{
            required: true,
            maxlength:100
        },
		role_category:{
            required: true,
            maxlength:100
        },
		Keyskills:{
            required: true,
            maxlength:100
        },
		industry:{
            required: true,
            maxlength:100
        },
		salary:{
            required: true,
            maxlength:50
        },
		country:{
            required: true,
            maxlength:50
        },
		state:{
            required: true,
            maxlength:50
        },
		city:{
            required: true,
            maxlength:50
        },
		no_of_openings:{
            required: true,
            maxlength:4
        }
	},messages:{
		job_title:{
			required:"Please enter job title",
			maxlength:"Maximum 100 characters please"
			},
		job_description:"Please enter job description",
		skills:{
			required:"Please enter required skills",
			maxlength:"Maximum 100 characters please"
			},
		experience:{
			required:"Please enter required experience",
			maxlength:"Maximum 50 characters please"
			},
		role:{
			required:"Please enter job role",
			maxlength:"Maximum 100 characters please"
			},
		role_category:{
			required:"Please enter job role category",
			maxlength:"Maximum 100 characters please"
			},
		Keyskills:{
			required:"Please enter job role category",
			maxlength:"Maximum 100 characters please"
			},
		industry:{
			required:"Please enter job role category",
			maxlength:"Maximum 100 characters please"
			},
		salary:{
			required:"Please enter the salary",
			maxlength:"Maximum 50 characters please"
			},
		country:{
			required:"Please enter country",
			maxlength:"Maximum 50 characters please"
			},
		state:{
			required:"Please enter state",
			maxlength:"Maximum 50 characters please"
			},
		city:{
			required:"Please enter city",
			maxlength:"Maximum 50 characters please"
			},
		no_of_openings:{
            required: "Please enter the number of openings",
            maxlength: "Please enter less than or equal to 5000 nos"
        }
	},
});

$("#id_apply_job").validate({
	rules:{
		name:{
			required:true,
			maxlength:50
		},
		mobile:{
			required:true,
			minlength: 10,
			maxlength:15,
			number: true
		},
        notice_period:{
			required:true,
			maxlength:50
		},
	},messages:{
		job_title:{
			required:"Please enter your name",
			maxlength:"Maximum 50 characters please"
			},
		mobile:{
			required:"Please enter your mobile no",
			minlength:"Mobile no should be of minimum 10 digits",
			maxlength:"Mobile no should be of maximum 15 digits",
			number:"Please enter your proper mobile no"
			},
		notice_period:{
			required:"Please enter your notice period",
			maxlength:"Maximum 50 characters please"
			},
	},
})