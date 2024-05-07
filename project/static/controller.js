let dte = new Date();

document.addEventListener('DOMContentLoaded', function(){
  let month = "{{ response.nameofmonth }}";
  let next_week = document.getElementById("nextweek");
  let last_week = document.getElementById("lastweek");
  let today;
  let crud = document.getElementById("crud");
  
  next_week.addEventListener('click', function(){
    let current_month = months[dte.getMonth()];
    if(window.location.search.includes("&nextmonth="))
    { 
      let next_month = months[months.indexOf(current_month) + 1];
      today = window.location.search.split("=")[1].replace("&nextmonth","");
      current_month = window.location.search.split("=")[2].replace("&nextmonth","");
      /*return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/weeksView?nextweek=${encodeURIComponent(today)}&nextmonth=${encodeURIComponent(next_month)}`;*/
    } else {
      if(window.location.search.includes("&nextweek="))
      {
        today = window.location.search.split("=")[1].replace("&nextmonth","");
      } else {
        today = dte.getDate();
      }
    }
    
    if(today < 7){
      today = '7';
    } 
    else if (today >= 7 && today < 14){
      today = '14';
    } 
    else if(today >= 14 && today < 21){
      today = '21';
    } 
    else if(today >= 21 && today < 28){
      today = '28';
    } 
    else if (today >= 28 && today < 31){
      today = '7';
      next_month = months[months.indexOf(current_month) + 1];
      current_month = next_month;
      return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/weeksView?nextweek=${encodeURIComponent(today)}&nextmonth=${encodeURIComponent(next_month)}`;
    }
    let date = Number(today);
    return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/weeksView?nextweek=${encodeURIComponent(date)}&nextmonth=${encodeURIComponent(current_month)}`;
  });
  
  last_week.addEventListener('click', function(){
    let current_month;
    let today;
    let prev_month = current_month;
    if(window.location.search.includes("&nextmonth="))
    { 
      let prev_month = months[months.indexOf(current_month) - 1];
      today = window.location.search.split("=")[1].replace("&nextmonth","");
      current_month = window.location.search.split("=")[2].replace("&nextmonth","");
      /*return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/weeksView?nextweek=${encodeURIComponent(today)}&nextmonth=${encodeURIComponent(next_month)}`;*/
    } else {
      today = window.location.search.split("=")[1].replace("&nextmonth","");
    }

    if(today <= 7){
      today = '28';
      prev_month = months[months.indexOf(current_month) - 1];
      current_month = prev_month;
    } 
    else if (today > 7 && today < 14){
      today = '7';
    } 
    else if(today >= 14 && today < 21){
      today = '7';
    } 
    else if(today >= 21 && today < 28){
      today = '14';
    } 
    else if (today >= 28 && today < 31){
      today = '21';
      return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/weeksView?nextweek=${encodeURIComponent(today)}&nextmonth=${encodeURIComponent(current_month)}`;
    }
    let date = Number(today);
    return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/weeksView?nextweek=${encodeURIComponent(date)}&nextmonth=${encodeURIComponent(current_month)}`;
    
    today = window.location.search.split("=")[1].replace("&nextmonth","");
    if(today < 31 && today > 28)
    {
      today = '28';
    } 
    else if(today <= 28 && today > 21)
    {
      today = '21';
    } 
    else if(today <= 21 && today > 14)
    {
      today = '14';
    } 
    else if(today <= 14 && today > 7)
    {
      today = '7';
    } else if(today <= 7) {
      let num = '7';
      return window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/weeksView?nextweek=${num}`;
    } else {
      today = '28'
    }
    date = today;
    window.location.href = `https://f8d46676-d318-40da-87b6-899cff4d6f58-00-1vvj5xa7dhwru.worf.replit.dev/weeksView?nextweek=${weekdateArray[date]}`;
  });
});