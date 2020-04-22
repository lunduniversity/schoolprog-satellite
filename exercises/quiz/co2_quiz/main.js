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

  //Create list to store feedback for all options in question 1:
  var fb_ls_q1 = ['Ungefär 0.04% av Jordens Atmosfär består av Koldioxid (CO\u2082).',
                  'Ungefär 20.95%'+' av Jordens Atmosfär består av Syre (O\u2082).',
                  'Korrekt! Ungefär 78% av Jordens Atmosfär består av Kväve (N\u2082). ',
                  'Ungefär 0.93% av Jordens Atmosfär består av Argon (Ar)'];

  //Create list to store feedback for all options in question 2:
  var fb_ls_q2 = ['Korrekt! N\u2082O frigörs bl.a. från kvävegödslad åkermark.',
                  'Korrekt! CO\u2082 frigörs bl.a. av förbränning av fossila bränslen.',
                  'O\u2082 är inte en växthusgas. Alla levande organismer behöver O\u2082 för att andas.',
                  'N\u2082 är inte en växthusgas. N\u2082 är den vanligaste gasen i jordens atmosfär.',
                  'Korrekt! CH\u2084 frigörs bl.a. från djurs matsmältningsprocess.'];

  //Create list to store feedback for all options in question 3:
  var fb_ls_q3 = ['Korrekt! Träd och vegetation tar upp CO\u2082 under fotosyntes.',
                  'Under oceanisk respiration släpps CO\u2082 ut från oceanerna.',
                  'Korrekt! Träd och vegetation tar upp CO\u2082 under fotosyntes.',
                  'Färre träd leder till minskat upptag av CO\u2082 för fotosyntes.',
                  'Korrekt! När havets växter fotosyntetiserar, tar de upp CO\u2082.',
                  'När växter andas släpper de ut CO\u2082.'];

  //Create list to store feedback for all options in question 4:
  var fb_ls_q4 = ['Korrekt! Skogsbränder ansvarar för större utsläpp av CO\u2082.',
                  'Korrekt! Vid volkanutbrott frigörs stora mängder CO\u2082 till atmosfären.',
                  'Korrekt! När döda kvistar & löv förrutnar släpps CO\u2082 ut till atmosfären.',
                  'Mer skog betyder mer växter som tar upp CO\u2082.',
                  'Korrekt! Förbränning av fossila bränlsen frigör CO\u2082.',
                  'Vid gödselhantering släpps metan (CH\u2084) och Lustgas ut (N\u2082O).'];

  //Create list to store feedback for all options in question 5:
  var fb_ls_q5 = ['Korrekt! Under vintertid ackumuleras CO\u2082,så på början av våren mäts de högsta CO\u2082-värdena.',
                  'Under sommaren ökar fotosyntesen och mer CO\u2082 tas upp från atmosfären.',
                  'Under hösten fotosyntetisera växter mindre och mindre CO\u2082 tas upp.',
                  'Under vintertid minskar fotosyntesen drastiskt och mindre CO\u2082 tas upp.'];

  //Create list to store feedback for all options in question 6:
  var fb_ls_q6 = ['Djurhållning ansvarar för större ustläpp av växthusgaser.',
                  'Förbränning av fossila bränslen ansvarar för större ustläpp av CO\u2082.',
                  'Skogsbränder ansvarar för större utsläpp av CO\u2082.',
                  'Korrekt! Under våren & sommaren tas mer CO\u2082 upp från växter p.g.a. fotosyntes. Som efterföljnad, mäts de lägsta CO₂-värdena under början på hösten.'];

  //Create list with ids of correct answers:
  var corr_ls = ["fb_q1c", "fb_q2a", "fb_q2b", "fb_q2e",
                 "fb_q3a", "fb_q3c", "fb_q3e",
                 "fb_q4a", "fb_q4b", "fb_q4c", "fb_q4e",
                 "fb_q5a", "fb_q6d"]

  //Function that
  function print_feedback(corr_ans_ls) {

    //Get a list of feedback-elements:
    var fb_ls = document.getElementsByName("feedback");

    //Loop through every list-element:
    for(var i=0;i<fb_ls.length;i++){

      //Make element visible:
      fb_ls[i].style.visibility = "visible";

      //Check if element-id corresponds to correct answer:
      if(corr_ans_ls.includes(fb_ls[i].id)){

        //Correct answer -- > Set color to "green":
        fb_ls[i].style.color = "#228B22";
      }
      else{
        //Wrong answer -- > Set color to "orange":
        fb_ls[i].style.color = "orange";
      }
    }
  }

  //Update content of HTML form:
  document.getElementById("after_submit").style.visibility = "visible";
  document.getElementById("message").innerHTML = messages[range];
  document.getElementById("number_correct").innerHTML = correct + "/6 rätta svar";
  document.getElementById("gif").src = gifs[range];

  //Feedback:
  document.getElementById("fb_q1a").innerHTML = fb_ls_q1[0];
  document.getElementById("fb_q1b").innerHTML = fb_ls_q1[1];
  document.getElementById("fb_q1c").innerHTML = fb_ls_q1[2];
  document.getElementById("fb_q1d").innerHTML = fb_ls_q1[3];

  document.getElementById("fb_q2a").innerHTML = fb_ls_q2[0];
  document.getElementById("fb_q2b").innerHTML = fb_ls_q2[1];
  document.getElementById("fb_q2c").innerHTML = fb_ls_q2[2];
  document.getElementById("fb_q2d").innerHTML = fb_ls_q2[3];
  document.getElementById("fb_q2e").innerHTML = fb_ls_q2[4];

  document.getElementById("fb_q3a").innerHTML = fb_ls_q3[0];
  document.getElementById("fb_q3b").innerHTML = fb_ls_q3[1];
  document.getElementById("fb_q3c").innerHTML = fb_ls_q3[2];
  document.getElementById("fb_q3d").innerHTML = fb_ls_q3[3];
  document.getElementById("fb_q3e").innerHTML = fb_ls_q3[4];
  document.getElementById("fb_q3f").innerHTML = fb_ls_q3[5];

  document.getElementById("fb_q4a").innerHTML = fb_ls_q4[0];
  document.getElementById("fb_q4b").innerHTML = fb_ls_q4[1];
  document.getElementById("fb_q4c").innerHTML = fb_ls_q4[2];
  document.getElementById("fb_q4d").innerHTML = fb_ls_q4[3];
  document.getElementById("fb_q4e").innerHTML = fb_ls_q4[4];
  document.getElementById("fb_q4f").innerHTML = fb_ls_q4[5];

  document.getElementById("fb_q5a").innerHTML = fb_ls_q5[0];
  document.getElementById("fb_q5b").innerHTML = fb_ls_q5[1];
  document.getElementById("fb_q5c").innerHTML = fb_ls_q5[2];
  document.getElementById("fb_q5d").innerHTML = fb_ls_q5[3];

  document.getElementById("fb_q6a").innerHTML = fb_ls_q6[0];
  document.getElementById("fb_q6b").innerHTML = fb_ls_q6[1];
  document.getElementById("fb_q6c").innerHTML = fb_ls_q6[2];
  document.getElementById("fb_q6d").innerHTML = fb_ls_q6[3];

  //Call function to make feedback-notes visible:
  print_feedback(corr_ls);

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

//Function that hides the content of all elements in a list:
function hide_item(item_list){
  if (item_list.length>0){
    for(var i=0;i<item_list.length;i++)
        item_list[i].style.visibility = "hidden";
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

  //Create variables to store a list of the feedback-notes for all questions:
  var fb_ls = document.getElementsByName("feedback");

  //Uncheck all elements in list:
  uncheck_item(q1_val_ls)
  uncheck_item(q2_val_ls)
  uncheck_item(q3_val_ls)
  uncheck_item(q4_val_ls)
  uncheck_item(q5_val_ls)
  uncheck_item(q6_val_ls)

  //Hide content from all elements in a list:
  hide_item(fb_ls)

  //Clear output messages:
  document.getElementById("message").innerHTML = "";
  document.getElementById("number_correct").innerHTML = "";
  document.getElementById("gif").src = "";
  document.getElementById("after_submit").style.visibility = "hidden"

  //Delete feedback:
  document.getElementsByName("feedback").innerHTML = "";
}


/*
#Create a list of feedbacks per option for every question:
q1_feedback = ['\033[1;93m'+'Ungefär 0.04% av Jordens Atmosfär består av Koldioxid (CO\u2082).'+'\033[1;93m',
               '\033[1;93m'+'Ungefär 20.95%'+' av Jordens Atmosfär består av Syre (O\u2082).'+'\033[1;93m',
               '\033[1;96m'+'Korrekt!\nUngefär 78% av Jordens Atmosfär består av Kväve (N\u2082). '+'\033[1;96m',
               '\033[1;93m'+'Ungefär 0.93% av Jordens Atmosfär består av Argon (Ar)'+'\033[1;93m']

q2_feedback = ['\033[1;96m'+'Korrekt! N\u2082O frigörs bl.a. från kvävegödslad åkermark.'+'\033[1;96m',
               '\033[1;96m'+'Korrekt! CO\u2082 frigörs bl.a. av förbränning av fossila bränslen.'+'\033[1;96m',
               '\033[1;93m'+'O\u2082 är inte en växthusgas. Alla levande organismer behöver O\u2082 för att andas.'+'\033[1;93m',
               '\033[1;93m'+'N\u2082 är inte en växthusgas. N\u2082 är den vanligaste gasen i jordens atmosfär.'+'\033[1;93m',
               '\033[1;96m'+'Korrekt! CH\u2084 frigörs bl.a. från djurs matsmältningsprocess.'+'\033[1;96m']

q3_feedback = ['\033[1;96m'+'Korrekt! Träd och vegetation tar upp CO\u2082 under fotosyntes.'+'\033[1;96m',
               '\033[1;93m'+'Under oceanisk respiration släpps CO\u2082 ut från oceanerna.'+'\033[1;93m',
               '\033[1;96m'+'Korrekt! Träd och vegetation tar upp CO\u2082 under fotosyntes.'+'\033[1;96m',
               '\033[1;93m'+'Färre träd leder till minskat upptag av CO\u2082 för fotosyntes.'+'\033[1;93m',
               '\033[1;96m'+'Korrekt! När havets växter fotosyntetiserar, tar de upp CO\u2082.'+'\033[1;96m',
               '\033[1;93m'+'När växter andas släpper de ut CO\u2082.'+'\033[1;93m']

q4_feedback = ['\033[1;96m'+'Korrekt! Skogsbränder ansvarar för större utsläpp av CO\u2082.'+'\033[1;96m',
               '\033[1;96m'+'Korrekt! Vid volkanutbrott frigörs stora mängder CO\u2082 till atmosfären.'+'\033[1;96m',
               '\033[1;96m'+'Korrekt! När döda kvistar & löv förrutnar släpps CO\u2082 ut till atmosfären.'+'\033[1;96m',
               '\033[1;93m'+'Mer skog betyder mer växter som tar upp CO\u2082.'+'\033[1;93m',
               '\033[1;96m'+'Korrekt! Vid förbränning av fossila bränlsen släpps CO\u2082 ut till atmosfären.'+'\033[1;96m',
               '\033[1;93m'+'Vid gödselhantering släpps metan (CH\u2084) och Lustgas ut (N\u2082O).'+'\033[1;93m']

q5_feedback = ['\033[1;96m'+'Korrekt!\nUnder vintertid ackumuleras CO\u2082.\nSom efterföljnad, mäts de högsta CO\u2082-värdena under början på våren.'+'\033[1;96m',
               '\033[1;93m'+'Under sommaren ökar fotosyntesen och mer CO\u2082 tas upp från atmosfären.\nPå det viset går den totala koncentrationen av CO₂ i Atmosfären ner.'+'\033[1;93m',
               '\033[1;93m'+'Under hösten börjar växter fotosyntetisera mindre och mindre CO\u2082 tas upp.\nDen totala koncentrationen av CO₂ i Atmosfären börjar gå upp.'+'\033[1;93m',
               '\033[1;93m'+'Under vintertid minskar fotosyntesen drastiskt och mindre CO\u2082 tas upp.\nDen totala koncentrationen av CO₂ i Atmosfären går upp.'+'\033[1;93m']

q6_feedback = ['\033[1;93m'+'Djurhållning ansvarar för större ustläpp av växthusgaser.'+'\033[1;93m',
               '\033[1;93m'+'Förbränning av fossila bränslen ansvarar för större ustläpp av CO\u2082.'+'\033[1;93m',
               '\033[1;93m'+'Skogsbränder ansvarar för större utsläpp av CO\u2082.'+'\033[1;93m',
               '\033[1;96m'+'Korrekt!\nUnder våren & sommaren tas mer CO\u2082 upp från växter p.g.a. fotosyntes.\nSom efterföljnad, mäts de lägsta CO₂-värdena under början på hösten.'+'\033[1;96m']

*/
