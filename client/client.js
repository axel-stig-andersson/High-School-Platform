var host = 'http://127.0.0.1:5000'
var signedIn = false
var nrOfCourses =  1 



function signedIN(){
    if (sessionStorage.getItem('auth') != null) {
        signedIn = sessionStorage.getItem('auth').length > 0;
        // document.getElementById("right_menu_button").innerHTML = '<a class="shop textfont" id="log_in" href="#" onclick="logOut() style="color:white;">Logga ut</a>'
    } 

} 
function logButton () {
    if (signedIn) {
        document.getElementById("right_menu_button").innerHTML = '<a class="shop textfont" id="log_out" href="#" onclick="logOut()" style="color:white;">Logga ut</a>'

    } else {
        document.getElementById("right_menu_button").innerHTML = '<a class="shop textfont" id="log_in" href="#" onclick="showLogInView()" style="color:white;">Logga in</a>'

    }
} 

function readMore(dot, readmore, readmoreRest, readmorebtn) {
        var dots = document.getElementById(dot);
        var moreText = document.getElementById(readmore);
        var btnText = document.getElementById(readmorebtn);
        var restText = document.getElementById(readmoreRest)
      
        if (dots.style.display === "none") {
          dots.style.display = "inline";
          btnText.innerHTML = "Läs vidare";
          moreText.style.display = "none";
          restText.style.display = "none";
        } else {
          dots.style.display = "none";
          btnText.innerHTML = "Läs mindre";
          moreText.style.display = "inline";
          restText.style.display= "inline";
        }
}
function charCounter(textarea, max) {
    var size = textarea.value.length
    if (size > max) {
        textarea.value = textarea.value.substring(0,500)
    } else {
    $("#currentCharAmount").text(size) 
    } 
    

}


$(document).ready(function () {
 
    

    $("#container").html($("#view_start").html());
    signedIN(); 
    logButton();

    $("#navbar_title").click(function (e) { 
        e.preventDefault(); 
        $("#container").html($("#view_start").html());
        // signedIN();  
        
    });


    $("#home_button").click(function (e) { 
        e.preventDefault();  
        loggedInOrNot()
        // $("#container").html($("#view_home").html()); 
        // signedIN();  
        
    });  
    $("#subjects_button").click(function (e) { 
        e.preventDefault();  
        
        $("#container").html($("#view_subjects").html());  
        // signedIN();  
        
    });  

    $("#contact_button").click(function (e) { 
        e.preventDefault();  
        
        $("#container").html($("#view_contact").html());  
        // signedIN();  
        
    });  
    $("#plan_button").click(function (e) { 
        e.preventDefault();  
        $("#container").html($("#view_plan").html());  
        // signedIN();  
        
    });  

    $("#log_in").click(function (e) {
        e.preventDefault();
        $("#container").html($("#view_login").html());  
        window.scrollTo(0, 0);       
    }); 
    $("#bp-home-link").click(function (e) { 
        e.preventDefault();  
        loggedInOrNot()
    }); 
    $("#bp-subjects-link").click(function (e) { 
        e.preventDefault();  
        $("#container").html($("#view_subjects").html());
    });   
    $("#bp-contact-link").click(function (e) { 
        e.preventDefault();  
        $("#container").html($("#view_contact").html());
    });  
    $("#bp-calcav-link").click(function (e) { 
        e.preventDefault();  
        $("#container").html($("#view_plan").html());
    });  
    $("#bp-calcreq-link").click(function (e) { 
        e.preventDefault();  
        $("#container").html($("#view_plan").html());
    });  
    $("#bp-tips-link").click(function (e) { 
        e.preventDefault();  
        $("#container").html($("#view_plan").html());
    });  


    




//     $("#women_link").click(function (e) {
//         e.preventDefault();
//         $("#container").html($("#view_shop").html());
//         hideAllWomens()
//         globalCust = "female";
//         filterSneakers();  
//         window.scrollTo(0, 0);      
//     });
});

function loggedInOrNot() {
    if (signedIn) {
        showAccount()
    } else {
        // $("#container").html($("#view_home").html());
        $("#login-to-show-home").modal(); 


    }}
    




function showAccount() {
    userId = JSON.parse(sessionStorage.getItem('auth')).user.id;
    $.ajax({
        url: host + '/users/' + userId,
        type: 'GET',
        headers: { "Authorization": "Bearer " + JSON.parse(sessionStorage.getItem('auth')).token },
        success: function(user) {
            $("#container").html($("#view_account").html());
            if (signedIn) {
                document.getElementById("profile-name").innerHTML = "Namn: " + user.name;
                document.getElementById("profile-program").innerHTML = "Studerar: " + user.education;
                document.getElementById("profile-grade").innerHTML = "Årskurs: " + user.grade;
                if (user.current_average == null) {
                    document.getElementById("profile-avg").innerHTML = "Betygssnitt: ---" ;
                } else {
                    document.getElementById("profile-avg").innerHTML = "Betygssnitt: " + user.current_average;
                }
                
            }  

        }
    })
    showMandCourses() 
    showFinishedCourses()

}



function signUp() {
    var pwd = checkPassword()
    
    date = new Date()
    $.ajax({
        url: host + '/signup',
        type: 'POST',
        contentType: "application/json",
        dataType: 'JSON',
        data: JSON.stringify({
           name: $("#inputSignUpName").val(), email: $("#inputSignUpEmail").val(), grade: $("#inputSignUpGrade").val(),
           birthdate: $("#inputSignUpBirthdate").val(), education: $("#inputSignUpProgram").val(),  password: pwd
        }), 
        success: function (data) {
            showLogInView()
        }
    
    })
}


function logIn() {
    $.ajax({
        url: host + '/login',
        type: 'POST',
        contentType: "application/json",
        dataType: 'JSON',
        data: JSON.stringify({
            email: $("#inputLogInEmail").val(), password: $("#inputLogInPassword").val()
        }),
        success: function (loginResponse) {
            sessionStorage.setItem('auth', JSON.stringify(loginResponse))
            signedIn = true;
            document.location.reload() 
            showAccount()
                   }
    })
}
function logOut() {
    userId = JSON.parse(sessionStorage.getItem('auth')).user.id;
    sessionStorage.removeItem('auth')
    signedIn = false;
    $("#container").html($("#view_start").html());
    document.location.reload()
}




function checkPassword() {
    pwd1 = $("#passwordInput1").val() 
    pwd2 = $("#inputSignUpPassword").val()

    if (pwd1 == pwd2) {
        return pwd1
    } else {
        showRegisterView()
        alert("Your passwords do not match - try again!");
        showRegisterView() 
    }
}


function showLogInView() {
    $("#container").html($("#view_login").html());
}

function showRegisterView() {
    $("#container").html($("#view_register").html()); 
} 

function showPlanView() {
    $("#container").html($("#view_plan").html())
}
function showCurrentView(){   
    // document.location.reload
}
function showSubjects() {
    $("#container").html($("#view_subjects").html())
}






function cleanFinished() { 
    userId = JSON.parse(sessionStorage.getItem('auth')).user.id;

    $.ajax ({
        url: host + '/resetfinished/' + userId,
        type: 'DELETE',
        contentType: 'application/json',
        dataType: 'JSON',
        data: JSON.stringify(userId),
        success: function(succeded) {

        } 
    })
}

function resetPlanView() {
    nrOfCourses = 1;
    showPlanView() 
}

function saveGrades() {
    userId = JSON.parse(sessionStorage.getItem('auth')).user.id;
    jsonStuff = {}
    for(i=0; i < nrOfCourses; i++) {
        couNr = i + 1;
        jsonStuff["nc"+i] = $("#inputC"+couNr+"").val()
    }
    for (j=0; j < nrOfCourses; j++) {
        graNr = j + 1;
        jsonStuff["ng"+j] = $("#inputB"+graNr+"").val()
    }
    $.ajax ({
        url: host + '/users/' + userId + '/finished', 
        type: 'POST', 
        contentType: 'application/json',
        dataType: 'JSON',
        data: JSON.stringify(jsonStuff),
        success: function (data) {
            console.log(data)
            if (data == "duplicate") {
                alert("Du har angivit samma kurs två gånger!")
            } 
        }
    })


}
function saveGradesAndAverage() {
    userId = JSON.parse(sessionStorage.getItem('auth')).user.id;
    if (userId == null) {
        alert("Du måste vara inloggad för att spara dina betyg")
    }
    else {
    saveGrades()
    var courseindexes = []; 
    var gradeindexes = [];
    var split = nrOfCourses*2
    var c = 1;
    var b = 1;
    for (i = 0; i < nrOfCourses; i++) {
        courseindexes.push(i)
    }
    for (i = nrOfCourses; i < split; i++) {
        gradeindexes.push(i) 
    }
    jdata = {}; 
    for (i in courseindexes) {
        var thisId = "#inputC"+c+"";
        c = c+1;
        jdata["v"+i]= $(thisId).val(); 
        // jdata[i]=thisId
    }
    for (j in gradeindexes) {
        var thisId2 = "#inputB"+b+"";
        b = b+1;
        jdata["v"+gradeindexes[j]]=$(thisId2).val();
    }

    $.ajax({
        url: host + '/average', 
        type: 'POST', 
        contentType: "application/json",
        dataType: 'JSON', 
        data: JSON.stringify(jdata),   
        
        success: function(data) { 
            var m = Number($("#merit-input").val())
            var gradePlusMerit = data + m 
            $.ajax({
                url: host + '/users/' + userId,
                type: "PUT",
                contentType:'application/json',
                dataType:'JSON',
                data: JSON.stringify({
                    current_average: gradePlusMerit
                }),
                success: function(data) {
                    resetPlanView() 
        
                }

            })

        }  
    }) 
}}

function calcAverage() {
    var courseindexes = [];
    var gradeindexes = [];
    var split = nrOfCourses*2
    var c = 1;
    var b = 1;
    for (i = 0; i < nrOfCourses; i++) {
        courseindexes.push(i)
    }
    for (i = nrOfCourses; i < split; i++) {
        gradeindexes.push(i) 
    }
    jdata = {}; 
    for (i in courseindexes) {
        var thisId = "#inputC"+c+"";
        c = c+1;
        jdata["v"+i]= $(thisId).val(); 
        // jdata[i]=thisId
    }
    for (j in gradeindexes) {
        var thisId2 = "#inputB"+b+"";
        b = b+1;
        jdata["v"+gradeindexes[j]]=$(thisId2).val();
    }
    console.log(jdata) 


    $.ajax({
        url: host + '/average', 
        type: 'POST', 
        contentType: "application/json",
        dataType: 'JSON', 
        data: JSON.stringify(jdata),   
        
        success: function(data) { 
            var m = Number($("#merit-input").val())
            var gradePlusMerit = data + m 
            if (signedIn == true) {
            var resultingdata = '<h3>Ditt snittbetyg är: <span id="merit-value">' + gradePlusMerit + '</span></h3><div class="btn btn-md btn-outline-light btn-primary" id="save_average" data-toggle="modal" data-target="#confirm-grade-save" style="margin: 10px;">Spara resultat</div><div class="btn btn-md btn-outline-light btn-primary" id="reset_calcaverage" style="margin: 10px;" onclick="resetPlanView()">Nollställ</div>' 
            } else {
            var resultingdata = '<h3>Ditt snittbetyg är: <span id="merit-value">' + gradePlusMerit + '</span></h3><p>Logga in för att spara det</p><div class="btn btn-md btn-outline-light btn-primary" id="reset-not-logged" style="margin: 10px;" onclick="resetPlanView()">Ok</div>'
            } 
            $("#av-result").append(resultingdata);   
        }  
    }) 
    const avb = document.getElementById('calcav-button')
    const lastbtn = document.getElementById('newcourse-button'+nrOfCourses)
    const lastbtnDiv = document.getElementById('newcourse-button-div'+nrOfCourses)
    avb.style.display = 'none'
    lastbtn.style.display='none'
    lastbtnDiv.style.display='none'
}

function addNewCourse() { 
    console.log(nrOfCourses);
    const btn = document.getElementById('newcourse-button'+nrOfCourses) 
    const btnDiv = document.getElementById('newcourse-button-div'+nrOfCourses) 
    nrOfCourses = nrOfCourses + 1 
        btn.style.display = 'none'  
        btnDiv.style.display ='none'  
    var newoption = '<div class="form-outline"><label class="form-label" for="inputC'+nrOfCourses+'">Kurstitel:&nbsp; </label><select id="inputC'+nrOfCourses+'">'
      +'<option value="Svenska 1">Svenska 1</option>'
      +'<option value="Svenska 2">Svenska 2</option>'
      +'<option value="Svenska 3">Svenska 3</option>'
      +'<option value="Engelska 5">Engelska 5</option>'
      +'<option value="Engelska 6">Engelska 6</option>'
      +'<option value="Engelska 7">Engelska 7</option>'
      +'<option value="Matematik 1c">Matematik 1c</option>'
      +'<option value="Matematik 2c">Matematik 2c</option>' 
      +'<option value="Matematik 3c">Matematik 3c</option>' 
      +'<option value="Matematik 4">Matematik 4</option>' 
      +'<option value="Matematik 5">Matematik 5</option>' 
      +'<option value="Historia 1">Historia 1</option>' 
      +'<option value="Religionskunskap 1">Religionskunskap 1</option>' 
      +'<option value="Samhällskunskap 1">Samhällskunskap 1</option>' 
      +'<option value="Geografi 1">Geografi 1</option>' 
      +'<option value="Samhällskunskap 2">Samhällskunskap 2</option>' 
      +'<option value="Historia 2">Historia 2</option>'
      +'<option value="Biologi 1"> Biologi 1</option>' 
      +'<option value="Biologi 2">Biologi 2</option>' 
      +'<option value="Kemi 1">Kemi 1</option>' 
      +'<option value="Kemi 2">Kemi 2</option>' 
      +'<option value="Fysik 1">Fysik 1</option>' 
      +'<option value="Fysik 2">Fysik 2</option>' 
      +'<option value="Finansiella beräkningar">Finansiella beräkningar</option>' 
      +'<option value="Idrott och Hälsa 1">Idrott och Hälsa 1</option>' 
      +'<option value="Matematik 1b">Matematik 1b</option>' 
      +'<option value="Matematik 2b">Matematik 2b</option>' 
      +'<option value="Matematik 3b">Matematik 3b</option>' 
      +'<option value="Moderna språk 1">Moderna språk 1</option>'  
      +'<option value="Idrott och Hälsa 2">Idrott och Hälsa 2</option>'
      +'<option value="Teknik 1">Teknik 1</option>' 
      +'<option value="Konstruktion 1">Konstruktion 1</option>' 
      +'<option value="Teknik 2">Teknik 2</option>' 
      +'<option value="Programmering 1">Programmering 1</option>' 
      +'<option value="Naturkunskap 1">Naturkunskap 1</option>' 
      +'<option value="Företagsekonomi 1">Företagsekonomi 1</option>' 
      +'<option value="Privatjuridik">Privatjuridik</option>' 
      +'<option value="Moderna språk 2">Moderna språk 2</option>' 
      +'<option value="Psykologi 1">Psykologi 1</option>' 
      +'<option value="Företagsekonomi 2">Företagsekonomi 2</option>' 
      +'<option value="Entreprenörskap och Företagande">Entreprenörskap och Företagande</option>' 
      +'<option value="Internationell ekonomi">Internationell ekonomi</option>' 
      +'<option value="Filosofi 1">Filosofi 1</option>' 
      +'<option value="Samhällskunskap 3">Samhällskunskap 3</option>' 
      +'<option value="Religionskunskap 2">Religionskunskap 2</option>' 
      +'<option value="Politik och Hållbar utveckling">Politik och Hållbar utveckling</option>' 
      +'<option value="Etnicitet och Kulturmöten">Etnicitet och Kulturmöten</option>' 
      +'<option value="Ledarskap och Organisation">Ledarskap och Organisation</option>' 
      +'<option value="Företagsekonomi Specialisering">Företagsekonomi Specialisering</option>' 
      +'<option value="Fysik 3">Fysik 3</option>' 
      +'<option value="Matematik Specialisering">Matematik Specialisering</option>' 
      +'<option value="Teknik Specialisering">Teknik Specialisering</option>' 
      +'<option value="Gymnasiearbete">Gymnasiearbete</option>'  
    +'</select>'
    +'<label class="form-label"for="inputB'+nrOfCourses+'">&nbsp; Betyg: </label>'
    +'<select id="inputB'+nrOfCourses+'">'
      +'<option value="A">A</option>'
      +'<option value="B">B</option>'
      +'<option value="C">C</option>' 
      +'<option value="D">D</option>'
      +'<option value="E">E</option>'
      +'<option value="F">F</option>' 
    +'</select>'
  +'</div>'
  +'<div class="newcourse-button-div" id="newcourse-button-div'+nrOfCourses+'">'
  +'<div class="btn btn-md btn-outline-light" id="newcourse-button'+nrOfCourses+'" onclick="addNewCourse()">'
    +'Lägg till kurs '
  +'</div>'
    +'</div>'

    $("#avcalc-form").append(newoption);    

}

function showMandCourses() {
    userId = JSON.parse(sessionStorage.getItem('auth')).user.id; 
    $.ajax({
        url: host + '/user/' + userId +'/mand',
        type: 'GET',

        success: function (mandatoryList) {
            $.ajax({
                url: host + '/user/' + userId +'/mand/points',
                type: 'GET',
                success: function (mandatoryPoints) {
                    $.ajax({
                        url: host + '/users/' + userId + '/mand/finished',
                        type: 'GET',
                        success: function(mandatoryRes) {
                            for (i in mandatoryList) {
                                var htmlData ='<tr><td>' + mandatoryList[i] + '</td><td>' + mandatoryPoints[i] + '</td><td>' + mandatoryRes[i] + '</td></tr>'
                                $("#man-cou-table-data").append(htmlData)
                            }
                        }
                    })
                }
            })
        } 
    })
}
function showFinishedCourses () {
    userId = JSON.parse(sessionStorage.getItem('auth')).user.id;
    $.ajax ({
        url : host + '/users/' + userId + '/finished',
        type: "GET",
        success:function (titles) {
            $.ajax({
                url : host + '/users/' + userId + '/points',
                type: "GET",
                success: function(points) {
                    $.ajax({
                        url: host + '/users/' + userId + '/grades',
                        type: "GET",
                        success: function(grades) {
                            for (i in titles) {
                                var dataToAppend = '<tr><td>' + titles[i] + '</td><td>' + points[i] + '</td><td>' + grades[i] + '</td></tr>'
                                $("#finishedcou-table-data").append(dataToAppend) 
                            }
                        }
                    })
                }
            })
        }
    })
}

function loadRemainingMand() {
    if (signedIn == false) {
        $("#must-log-in").modal(); 
    } else {
    userId = JSON.parse(sessionStorage.getItem('auth')).user.id;
    const loadbtn = document.getElementById("load-mandatory-btn")
    loadbtn.style.display = 'none';
    var counter = 0

    $.ajax({
        url: host + '/users/' + userId + '/mand/remaining',
        type: 'GET',
        success: function(remainingTitles) {
            for (i in remainingTitles) {
                var cTitle = '<div class="form-outline"><label class="form-label" for="inputR'+i+'">Kurstitel:   </label><select class="rem-inputs" id="inputR'+i+'">'
                +'<option value="'+ remainingTitles[i]+'">'+remainingTitles[i]+'</option>'
              +'</select>'
                $("#courses-to-read-inner").append(cTitle)    
                counter = counter + 1
            } 
            console.log(counter)
            var newCouBtn ='<div class="btn btn-md btn-outline-light btn-primary" id="newcb'+counter+'" onclick="startNewUnfinished('+counter+')">'
            +'Lägg till kurs '
            +'</div>'
            $("#courses-to-read-inner").append(newCouBtn)

            var meritInputNew = '<div class="form-outline">'
            +'<label class="form-label" for="merit-input-final">Meritpoäng: </label>'
            +'<select id="merit-input-final" aria-describedby="merit-explained-unfinished">'
            +'<option value="0.0">0</option>'
            +'<option value="0.5">0.5</option>'
            +'<option value="1.0">1.0</option>'
            +'<option value="1.5">1.5</option>'
            +'<option value="2.0">2.0</option>'
            +'<option value="2.5">2.5</option>'
            +'</select>' 
            +'<small id="merit-explained-unfinished" class="form-text text-muted">Vilka kurser som ger meritpoäng samt hur mycket beror på vilken utbildning du vill läsa.</small>'
            +'</div>'
            var goalAverageInput = '<div class="form-outline">'
            +'<label for="required-average-input">Jag vill ha betygssnittet:</label>'
            +'<input type="number" class="form-control" id="required-average-input" aria-describedby="req-av-description">'
            +'<small id="req-av-description" class="form-text text-muted">Ange en siffra, decimaler anges med "." (punkt)</small>'
            +'</div>'
            var calcResBtn = '<div class="btn btn-md btn-outline-light btn-primary" id="calc-required-grades" onclick="lengthHelpFunc()">'
            +'Beräkna krav'
            +'</div>'
            $("#courses-to-read-bottom").append(meritInputNew)
            $("#courses-to-read-bottom").append(goalAverageInput)
            $("#courses-to-read-bottom").append(calcResBtn)
        }
    })
}
}
function lengthHelpFunc() {
    var tot = document.getElementById("courses-to-read-inner").querySelectorAll(".rem-inputs")
    thislength = tot.length
    calcRequiredGrades(thislength)

}

function calcRequiredGrades(nrOfRemainingCourses) {
    userId = JSON.parse(sessionStorage.getItem('auth')).user.id;
    reqAverage = $("#required-average-input").val()
    final_merit = $("#merit-input-final").val()
    coursesInputJson = {}
    coursesInputTitle = []
    for (i = 0; i < nrOfRemainingCourses; i++) {
        coursesInputJson["r"+i] = $("#inputR"+i+"").val()
        coursesInputTitle.push($("#inputR"+i+"").val())
    }
    $.ajax ({
        url: host + '/users/' + userId + '/required-grades/' + reqAverage + "/" + final_merit,
        type: 'POST',
        contentType: 'application/json',
        dataType: 'JSON',
        data: JSON.stringify(coursesInputJson),
        success: function(response) {
            if (response == "no") {
                alert("För få kurser!")
            } else {
                var allgrades = ""
                const currentview = document.getElementById("courses-to-read-outer")
                const currentViewBottom = document.getElementById("courses-to-read-bottom")
                currentview.style.display = 'none';
                currentViewBottom.style.display= 'none';
                for (i = 0; i < nrOfRemainingCourses; i++) {
                    req = '<tr><td>' + coursesInputTitle[i] + '</td><td>' + response[i] + '</td></tr>'
                    allgrades = allgrades + req;
                }
                var newHTML = '<div class="container flex-container" id="result-required-container"' 
                +'<h4 style="color:black;">Om du exempelvis får dessa betyg kommer du att nå ditt mål: </h4>'
                +'<table class="table table-striped" id="required-grades-table">'
                +'<thead>'
                 +'<tr>'
                    +'<th scope="col">Kurstitel</th>'
                    +'<th scope="col">Betyg</th>'
                  +'</tr>'
                +'</thead>'
               +'<tbody id="man-cou-table-data">' 
               + allgrades 
                +'</tbody>'

              +'</table>'
              +'<div class="btn btn lg btn-outline-dark" id="reset-req-grades" onclick="showPlanView()">Nollställ</div>'
              +'</div>'

              $("#courses-gradeplan-column").append(newHTML)

            }
        }
    })
}

function startNewUnfinished (coursesAdded) {
    console.log(coursesAdded)
    userId = JSON.parse(sessionStorage.getItem('auth')).user.id;
    newCounter = coursesAdded
    oldButton = document.getElementById("newcb"+coursesAdded+"")
    oldButton.style.display = 'none';  

    $.ajax ({
        url: host + '/users/' + userId + '/all-remaining',
        type: 'GET',
        success: function(courseList) {
            addNewUnfinished(courseList, newCounter)
        }
    }) 
}

function addNewUnfinished(list, nr) {
    var allOptions = ""
    for (i in list) {
        opt = '<option value="'+ list[i]+'">'+list[i]+'</option>'
        allOptions = allOptions + opt 
    }
    var newInput = '<div class="form-outline"><label class="form-label" for="inputR'+nr+'">Kurstitel: </label><select class="rem-inputs" id="inputR'+nr+'">'
    +allOptions+'</select></div>'
    newNr = Number(nr) + Number(1);
    var newCouBtn ='<div class="btn btn-md btn-outline-light btn-primary" id="newcb'+newNr+'" onclick="startNewUnfinished('+newNr+')">'
    +'Lägg till kurs '
    +'</div>'
    $("#courses-to-read-inner").append(newInput)
    $("#courses-to-read-inner").append(newCouBtn) 
}

function sendCourseRequest() {
    if (signedIn == false) {
        $("#not-received-confirmation").modal(); 
        return "none"
    } else {
    console.log("öppnade andra?")
    userId = JSON.parse(sessionStorage.getItem('auth')).user.id;
    $.ajax ({
        url: host + "/contact-us/" + userId + "/course-suggestion",
        type: 'POST',
        contentType: 'application/json',
        dataType: 'JSON',
        data: JSON.stringify({
            course_title: $("#inputCourseSuggestTitle").val(), points: $("#inputCourseSuggestPoints").val(), kommun: $("#inputCourseSuggestKommun").val(), school: $("#inputCourseSuggestSchool").val()
        }),
        success: function(data) {
            $("#logged-in-received-confirmation").modal(); 

        }
    })}

}
function sendOtherRequest() {
    if (signedIn == false) {
        $("#not-received-confirmation").modal(); 
        return "none"
    } else {
    userId=JSON.parse(sessionStorage.getItem('auth')).user.id;
    $.ajax ({
        url: host + "/contact-us/" + userId + "/other-suggestion",
        type: 'POST',
        contentType: 'application/json',
        dataType:'JSON',
        data: JSON.stringify({
        request_type: $("#inputOtherSuggestCategory").val(), message: $("#inputOtherSuggest").val()
        }), success: function(data) {
                $("#logged-in-received-confirmation").modal();


        }
    })
}
}

