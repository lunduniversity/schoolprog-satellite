function check(){

  //Get user input for every question in the form
  //Question 1:
  var question1 = document.quiz.q1.value;

  //Question 2:
  var question2a = document.getElementById("q2_n2o").checked;
  var question2b = document.getElementById("q2_co2").checked;
  var question2c = document.getElementById("q2_o2").checked;
  var question2d = document.getElementById("q2_n2").checked;
  var question2e = document.getElementById("q2_ch4").checked;

  //Question 3:
  var question3a = document.getElementById("q3_vegetation").checked;
  var question3b = document.getElementById("q3_oceanic_respiration").checked;
  var question3c = document.getElementById("q3_reforestation").checked;
  var question3d = document.getElementById("q3_deforestation").checked;
  var question3e = document.getElementById("q3_oceanic_photosynthesis").checked;
  var question3f = document.getElementById("q3_vegetation_respiration").checked;

  //Question 4:
  var question4a = document.getElementById("q4_forest_fires").checked;
  var question4b = document.getElementById("q4_volcanoes").checked;
  var question4c = document.getElementById("q4_animal_plant_decay").checked;
  var question4d = document.getElementById("q4_reforestation").checked;
  var question4e = document.getElementById("q4_burning_fossil_fuels").checked;
  var question4f = document.getElementById("q4_manure").checked;

  //Question 5:
  var question5 = document.quiz.q5.value;

  //Question 6:
  var question6 = document.quiz.q6.value;

  //Define variable to store correct answers:
  var correct = 0;

  //Check answers (radiobuttons):
  if (question1 == "n2"){
    correct++;
  }

  if (question5 == "spring"){
    correct++;
  }

  if (question6 == "photosynthesis"){
    correct++;
  }

  //Check answers (checkboxes):
  if (question2a && question2b && question2e){
    correct++;
  }

  if (question3a && question3c && question3e){
    correct++;
  }

  if (question4a && question4b && question4c && question4e){
    correct++;
  }


  //Store output messages in list:
  var messages = ["Hoppsan!<br>Dags att börja tänka på klimatet...",
                  "Bra!<br>Du har tagit första steget till att bli mer klimatmedveten.<br>Ta nästa skutt och inspirera andra göra samma sak!",
                  "Bra jobbat!<br>Du är klimatmedveten.<br>Dela din kunskap med andra!",
                  "Gratulerar!<br>Du är en riktig klimatmästare!!!"];

  //Create list to store output gifs:
  var gifs = ["gifs/oops.gif", "gifs/novisch.gif",
              "gifs/climate_aware.gif", "gifs/champion.gif"];

  //Declare variable to store index number for list of messages:
  var range;

  //Assign every message in list to corresponding number of correct answers:
  if (correct < 3){
    range = 0
  }
  else if (correct > 2 && correct < 4) {
    range = 1
  }
  else if (correct > 3 && correct < 6) {
    range = 2
  }
  else{
    range = 3
  }



  //Update content of HTML form:
  document.getElementById("after_submit").style.visibility = "visible";
  document.getElementById("message").innerHTML = messages[range];
  document.getElementById("number_correct").innerHTML = correct + "/6 rätta svar";
  document.getElementById("gif").src = gifs[range];

  //Jump to location:
  var elmnt = document.getElementById("after_submit");
  elmnt.scrollIntoView();
}



//Function that unchecks all elements in a list:
function uncheck_item(item_list){
  if (item_list.length>0){
    for(var i=0;i<item_list.length;i++)
        item_list[i].checked = false;
  }
  else{
    console.log("Cannot uncheck list element!")
  }
}



//Function that cleans the form from all inputs:
function init(){

  //Create variables to store a list of the checkbox-elements per question:
  var q1_val_ls = document.getElementsByName("q1");
  var q2_val_ls = document.getElementsByName("q2");
  var q3_val_ls = document.getElementsByName("q3");
  var q4_val_ls = document.getElementsByName("q4");
  var q5_val_ls = document.getElementsByName("q5");
  var q6_val_ls = document.getElementsByName("q6");

  //Uncheck all elements in list:
  uncheck_item(q1_val_ls)
  uncheck_item(q2_val_ls)
  uncheck_item(q3_val_ls)
  uncheck_item(q4_val_ls)
  uncheck_item(q5_val_ls)
  uncheck_item(q6_val_ls)

  //Clear output messages:
  document.getElementById("message").innerHTML = "";
  document.getElementById("number_correct").innerHTML = "";
  document.getElementById("gif").src = "";
  document.getElementById("after_submit").style.visibility = "hidden"
}


