

$(document).ready(function() {
    $('#sign_in_form').bootstrapValidator({
        message: 'This value is not valid',
        fields: {
            username: {
                validators: {
                    notEmpty: {
                        message: 'Please input your user name or email address.'
                    },
                    emailAddress: {
                        message: 'Please input a valid email address.'
                    }
                }
            },
            password: {
                validators: {
                    notEmpty: {
                        message: 'Please input password.'
                    }
                }
            }
        }
    });

    $('#sign_up_form').bootstrapValidator({
        message: 'This value is not valid',
        fields: {
            email: {
                validators: {
                    notEmpty: {
                        message: 'Please input a valid email address.'
                    },
                    emailAddress: {
                        message: 'Please input a valid email address.'
                    }
                }
            },
            firstname: {
                validators: {
                    nonEmpty: {
                        message: 'Please input your name.'
                    }
                }
            },
            lastname: {
                validators: {
                    nonEmpty: {
                        message: 'Please input your name.'
                    }
                }
            },
            password: {
                validators: {
                    notEmpty: {
                        message: 'Please input password.'
                    },
                }
            },
            confirmPassword: {
                validators: {
                    notEmpty: {
                        message: 'Please input password.'
                    },
                    identical: {
                        field: 'password',
                        message: 'Password inputs should be identical.'
                    },
                }
            },
        }
    });

    $('body').on('click', '#sign-in-btn', function(e) {
        e.preventDefault();
        alert("sign in!"); 
        $("#sign-in-error-msg").text('');
        // use dummy string is you are using 2-column layout
        //var session_string = $('#statement-btn').hasClass('highlight-nav-btn') ? '' : getState();
        $.ajax({
            url: 'login/',
            type: 'post',
            data: {
                username: $("#sign-in-email").val(),
                password: $("#sign-in-password").val(),
                //session_string: session_string,
            },
            success: function(xhr) {
                $("#authentication_modal").modal('hide');
                alert("!!!");
                if (xhr.url) { // I'm in forum selection page and I'll jump to my last forum
                    window.location.replace(xhr.url);

                }
                
                $("#curr-user-id").attr('value',(xhr.user_id));
                $("#curr-user-name").html(xhr.user_name);

           },
            error: function(xhr) {
                alert("error!");
                $("#sign-in-error-msg").text(xhr.responseText);
            }
        });
    });

    $('body').on('click', '#sign-up-btn', function(e) {
        e.preventDefault();

        $("#sign-up-error-msg").text('');
        
        $.ajax({
            url: 'register/',
            type: 'post',
            data: {
                firstname: $("#sign-up-firstname").val(),
                lastname: $("#sign-up-lastname").val(),
                email: $("#sign-up-email").val(),
                password: $("#sign-up-password").val(),
                userinfo: $("#sign-up-userinfo").val(),
                //session_string: session_string
            },

            success: function(xhr) {
                $("#authentication_modal").modal('hide');
                $("#curr-user-id").html(xhr.user_id);
                $("#curr-user-name").html(xhr.user_name);
            },

            error: function(xhr) {
                $("#sign-up-error-msg").text(xhr.responseText);
            }
        });
    });

    $('body').on('click', '#logout-btn', function(e) {
        e.preventDefault();
        alert("you are going to logout"); 
        $.ajax({
            url: 'logout/',
            type: 'POST',
            complete: function() {
                $("#curr-user-id").html('-1');
                $("#curr-user-name").html('Visitor');
                
            }
        });
    });

});
